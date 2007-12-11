import os
try:
    import sqlite3
except ImportError:
    from pysqlite2 import dbapi2 as sqlite3

from zope.interface import implements

from interfaces import IRelationalDatabase

class RelationalDatabase(object):

    implements(IRelationalDatabase)

    def __init__(self):
        curdir = os.path.abspath(os.path.dirname(__file__))
        db_file = os.path.join(curdir, 'RData.db')
        self.conn = sqlite3.connect(db_file)
        self.conn.row_factory = sqlite3.Row

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def cursor(self):
        return self.conn.cursor()

    def get_next_id(self, table):
        cr = self.cursor()
        cr.execute("""SELECT max(id) as max_id FROM %s""" % table)
        record = cr.fetchone()
        cr.close()
        if record['max_id']:
            return record['max_id'] + 1
        else:
            return 1
