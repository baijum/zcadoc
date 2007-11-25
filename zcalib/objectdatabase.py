import os
from ZODB import FileStorage, DB
import transaction
from BTrees.OOBTree import OOBTree
from BTrees.IOBTree import IOBTree

from zope.interface import implements

from interfaces import IObjectDatabase

class ObjectDatabase(object):

    implements(IObjectDatabase)

    def __init__(self):
        curdir = os.path.abspath(os.path.dirname(__file__))
        db_file = os.path.join(curdir, 'OData.db')
        storage = FileStorage.FileStorage(db_file)
        db = DB(storage)
        conn = db.open()
        self.dbroot = conn.root()
        if 'zcalibdb' not in self.dbroot:
            self.dbroot['zcalibdb'] = OOBTree()
            zcalibdb = self.dbroot['zcalibdb']
            zcalibdb['members'] = IOBTree()
            zcalibdb['books'] = IOBTree()
            zcalibdb['circulations'] = IOBTree()
            self.commit()

    def commit(self):
        transaction.commit()

    def rollback(self):
        transaction.abort()

    def container(self):
        return self.dbroot['zcalibdb']

    def get_next_id(self, container_name):
        zcalibdb = self.container()
        try:
            return max(zcalibdb[container_name].keys()) + 1
        except ValueError:
            return 1
