from zope.component import getGlobalSiteManager

from database import Database
from member import MemberDbOperation
from catalog import BookDbOperation
from circulation import CirculationDbOperation

from interfaces import IDatabase
from interfaces import IMember
from interfaces import IBook
from interfaces import ICirculation
from interfaces import IDbOperation

def initialize():
    
    gsm = getGlobalSiteManager()
    db = Database()
    gsm.registerUtility(db, IDatabase)

    gsm.registerAdapter(MemberDbOperation,
                        (IMember,),
                        IDbOperation)

    gsm.registerAdapter(BookDbOperation,
                        (IBook,),
                        IDbOperation)

    gsm.registerAdapter(CirculationDbOperation,
                        (ICirculation,),
                        IDbOperation)
    
def finalize():
    pass

