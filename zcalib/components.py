from zope.interface import implements

from interfaces import IBook
from interfaces import IMember
from interfaces import ICirculation

class Book(object):

    implements(IBook)

    barcode = ""
    title = ""
    author = ""

class Member(object):

    implements(IMember)

    number = ""
    name = ""

class Circulation(object):

    implements(ICirculation)

    book = Book()
    member = Member()
