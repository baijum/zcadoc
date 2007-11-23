from zope.interface import implements
from zope.component import getUtility
from zope.component import adapts

from components import Circulation

from interfaces import IDatabase
from interfaces import ICirculation
from interfaces import IDbOperation


class CirculationDbOperation(object):

    implements(IDbOperation)
    adapts(ICirculation)

    def __init__(self, circulation):
        self.circulation = circulation

    def get(self):
        db = getUtility(IDatabase)
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
        db = getUtility(IDatabase)
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
        db = getUtility(IDatabase)
        cr = db.cursor()
        book_id = self.circulation.book.id
        cr.execute("""DELETE FROM circulations
                      WHERE book_id = ?""",
                   (book_id,))
        cr.close()
        db.commit()
