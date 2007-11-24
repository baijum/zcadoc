import os
import gtk
import gtk.glade

from zope.component import getAdapter

from components import Member
from components import Book
from components import Circulation
from interfaces import IDbOperation


class CirculationWindow(object):

    def __init__(self):
        curdir = os.path.abspath(os.path.dirname(__file__))
        xml = os.path.join(curdir, 'glade', 'circulationwindow.glade')
        xmlobj = gtk.glade.XML(xml)

        self.circulationwindow = xmlobj.get_widget('circulationwindow')
        self.issue_member = xmlobj.get_widget('issue_member')
        self.issue_book = xmlobj.get_widget('issue_book')
        self.return_book = xmlobj.get_widget('return_book')
        issue_button = xmlobj.get_widget('issue_button')
        return_button = xmlobj.get_widget('return_button')

        self.circulationwindow.connect('delete_event', self.on_delete_event)
        issue_button.connect('clicked', self.on_issue_clicked)
        return_button.connect('clicked', self.on_return_clicked)


    def show_all(self):
        self.circulationwindow.show_all()

    def on_delete_event(self, *args):
        self.circulationwindow.hide()
        return True

    def on_issue_clicked(self, *args):
        member_number = self.issue_member.get_text()
        book_barcode = self.issue_book.get_text()
        self.book_issue(member_number, book_barcode)

    def book_issue(self, member_number, book_barcode):
        member = Member()
        member.number = member_number
        memberdboperation = getAdapter(member, IDbOperation)
        member = memberdboperation.get()[0]

        book = Book()
        book.number = book_barcode
        bookdboperation = getAdapter(book, IDbOperation)
        book = bookdboperation.get()[0]

        circulation = Circulation()
        circulation.member = member
        circulation.book = book
        circulationdboperation = getAdapter(circulation, IDbOperation)
        circulationdboperation.add()

    def on_return_clicked(self, *args):
        book_barcode = self.return_book.get_text()
        self.book_return(book_barcode)

    def book_return(self, book_barcode):
        book = Book()
        book.number = book_barcode
        bookdboperation = getAdapter(book, IDbOperation)
        book = bookdboperation.get()[0]

        circulation = Circulation()
        circulation.book = book
        circulationdboperation = getAdapter(circulation, IDbOperation)
        circulationdboperation.delete()

    
circulationwindow = CirculationWindow()
