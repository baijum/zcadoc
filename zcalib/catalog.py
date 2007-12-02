from zope.interface import implements
from zope.component import getUtility
from zope.component import adapts

from components import Book

from interfaces import IRelationalDatabase
from interfaces import IObjectDatabase
from interfaces import IBook
from interfaces import IDbOperation


class BookRDbOperation(object):

    implements(IDbOperation)
    adapts(IBook)

    def __init__(self, book):
        self.book = book

    def get(self):
        db = getUtility(IRelationalDatabase)
        cr = db.cursor()
        barcode = self.book.barcode
        if barcode:
            cr.execute("""SELECT
                            id,
                            barcode,
                            author,
                            title
                          FROM books
                          WHERE barcode = ?""",
                       (barcode,))
        else:
            cr.execute("""SELECT
                            id,
                            barcode,
                            author,
                            title
                          FROM books""")
        rst = cr.fetchall()
        cr.close()
        books = []
        for record in rst:
            id = record['id']
            barcode = record['barcode']
            author = record['author']
            title = record['title']
            book = Book()
            book.id = id
            book.barcode = barcode
            book.author = author
            book.title = title
            books.append(book)
        return books

    def add(self):
        db = getUtility(IRelationalDatabase)
        cr = db.cursor()
        next_id = db.get_next_id("books")
        barcode = self.book.barcode
        author = self.book.author
        title = self.book.title
        cr.execute("""INSERT INTO books
                        (id, barcode, author, title)
                      VALUES (?, ?, ?, ?)""",
                   (next_id, barcode, author, title))
        cr.close()
        db.commit()
        self.book.id = next_id

    def update(self):
        db = getUtility(IRelationalDatabase)
        cr = db.cursor()
        barcode = self.book.barcode
        author = self.book.author
        title = self.book.title
        id = self.book.id
        cr.execute("""UPDATE books
                        SET
                            barcode = ?,
                            author = ?,
                            title = ?
                      WHERE id = ?""",
                   (barcode, author, title, id))
        cr.close()
        db.commit()

    def delete(self):
        db = getUtility(IRelationalDatabase)
        cr = db.cursor()
        id = self.book.id
        cr.execute("""DELETE FROM books
                      WHERE id = ?""",
                   (id,))
        cr.close()
        db.commit()


class BookODbOperation(object):

    implements(IDbOperation)
    adapts(IBook)

    def __init__(self, book):
        self.book = book

    def get(self):
        db = getUtility(IObjectDatabase)
        zcalibdb = db.container()
        books = zcalibdb['books']
        return books.values()

    def add(self):
        db = getUtility(IObjectDatabase)
        zcalibdb = db.container()
        books = zcalibdb['books']
        barcode = self.book.barcode
        if barcode in [x.barcode for x in books.values()]:
            db.rollback()
            raise Exception("Duplicate key")
        next_id = db.get_next_id('books')
        self.book.id = next_id
        books[next_id] = self.book
        db.commit()

    def update(self):
        db = getUtility(IObjectDatabase)
        zcalibdb = db.container()
        books = zcalibdb['books']
        id = self.book.id
        books[id] = self.book
        db.commit()

    def delete(self):
        db = getUtility(IObjectDatabase)
        zcalibdb = db.container()
        books = zcalibdb['books']
        id = self.book.id
        del books[id]
        db.commit()
