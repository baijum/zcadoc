from zope.interface import implements
from zope.component import getUtility
from zope.component import adapts

from components import Circulation

from interfaces import IRelationalDatabase
from interfaces import IObjectDatabase
from interfaces import ICirculation
from interfaces import IDbOperation


class CirculationRDbOperation(object):

    implements(IDbOperation)
    adapts(ICirculation)

    def __init__(self, circulation):
        self.circulation = circulation

    def get(self):
        db = getUtility(IRelationalDatabase)
        cr = db.cursor()
        id = self.circulation.id
        if id:
            cr.execute("""SELECT
                            id,
                            member_id,
                            book_id
                          FROM circulations
                          WHERE id = ?""",
                       (id,))
        else:
            cr.execute("""SELECT
                            id,
                            member_id,
                            book_id
                          FROM circulations""")
        rst = cr.fetchall()
        cr.close()
        circulations = []
        for record in rst:
            id = record['id']
            member_id = record['member_id']
            book_id = record['book_id']
            circulation = Circulation()
            circulation.id = id
            circulation.member_id = member_id
            circulation.book_id = book_id
            circulations.append(circulation)
        return circulations

    def add(self):
        db = getUtility(IRelationalDatabase)
        cr = db.cursor()
        next_id = db.get_next_id("circulations")
        member_id = self.circulation.member.id
        book_id = self.circulation.book.id
        cr.execute("""INSERT INTO circulations
                        (id, member_id, book_id)
                      VALUES (?, ?, ?)""",
                   (next_id, member_id, book_id))
        cr.close()
        db.commit()
        self.circulation.id = next_id

    def update(self):
        pass

    def delete(self):
        db = getUtility(IRelationalDatabase)
        cr = db.cursor()
        book_id = self.circulation.book.id
        cr.execute("""DELETE FROM circulations
                      WHERE book_id = ?""",
                   (book_id,))
        cr.close()
        db.commit()


class CirculationODbOperation(object):

    implements(IDbOperation)
    adapts(ICirculation)

    def __init__(self, circulation):
        self.circulation = circulation

    def get(self):
        db = getUtility(IObjectDatabase)
        zcalibdb = db.container()
        circulations = zcalibdb['circulations']
        return circulations.values()

    def add(self):
        db = getUtility(IObjectDatabase)
        zcalibdb = db.container()
        circulations = zcalibdb['circulations']
        barcode = self.circulation.book.barcode
        if barcode in [x.book.barcode for x in circulations.values()]:
            db.rollback()
            raise Exception("Duplicate key")
        book_id = self.circulation.book.id
        circulations[book_id] = self.circulation
        db.commit()

    def update(self):
        pass

    def delete(self):
        db = getUtility(IObjectDatabase)
        zcalibdb = db.container()
        circulations = zcalibdb['circulations']
        id = self.circulation.book.id
        del circulations[id]
        db.commit()
