import os
import gtk
import gtk.glade

from zope.component import getAdapter

from components import Book
from interfaces import IDbOperation


class CatalogWindow(object):

    def __init__(self):
        curdir = os.path.abspath(os.path.dirname(__file__))
        xml = os.path.join(curdir, 'glade', 'catalogwindow.glade')
        xmlobj = gtk.glade.XML(xml)

        self.catalogwindow = xmlobj.get_widget('catalogwindow')

        self.barcode = xmlobj.get_widget('barcode')
        self.author = xmlobj.get_widget('author')
        self.title = xmlobj.get_widget('title')
        add = xmlobj.get_widget('add')
        update = xmlobj.get_widget('update')
        delete = xmlobj.get_widget('delete')
        close = xmlobj.get_widget('close')
        self.treeview = xmlobj.get_widget('treeview')

        self.catalogwindow.connect('delete_event', self.on_delete_event)
        add.connect('clicked', self.on_add_clicked)
        update.connect('clicked', self.on_update_clicked)
        delete.connect('clicked', self.on_delete_clicked)
        close.connect('clicked', self.on_delete_event)

        self.initialize_list()

    def show_all(self):
        self.populate_list_store()
        self.catalogwindow.show_all()

    def populate_list_store(self):
        self.list_store.clear()
        book = Book()
        bookdboperation = getAdapter(book, IDbOperation)
        books = bookdboperation.get()
        for book in books:
            barcode = book.barcode
            author = book.author
            title = book.title
            self.list_store.append((book, barcode, author, title))

    def on_delete_event(self, *args):
        self.catalogwindow.hide()
        return True

    def initialize_list(self):
        self.list_store = gtk.ListStore(object, str, str, str)
        self.treeview.set_model(self.list_store)

        tvcolumn = gtk.TreeViewColumn('Barcode')
        self.treeview.append_column(tvcolumn)

        cell = gtk.CellRendererText()
        tvcolumn.pack_start(cell, True)
        tvcolumn.add_attribute(cell, 'text', 1)

        tvcolumn = gtk.TreeViewColumn('Author')
        self.treeview.append_column(tvcolumn)

        cell = gtk.CellRendererText()
        tvcolumn.pack_start(cell, True)
        tvcolumn.add_attribute(cell, 'text', 2)

        tvcolumn = gtk.TreeViewColumn('Title')
        self.treeview.append_column(tvcolumn)

        cell = gtk.CellRendererText()
        tvcolumn.pack_start(cell, True)
        tvcolumn.add_attribute(cell, 'text', 3)

    def on_add_clicked(self, *args):
        barcode = self.barcode.get_text()
        author = self.author.get_text()
        title = self.title.get_text()
        book = Book()
        book.barcode = barcode
        book.author = author
        book.title = title
        self.add(book)
        self.list_store.append((book, barcode, author, title))

    def add(self, book):
        bookdboperation = getAdapter(book, IDbOperation)
        bookdboperation.add()

    def on_update_clicked(self, *args):
        barcode = self.barcode.get_text()
        author = self.author.get_text()
        title = self.title.get_text()
        treeselection = self.treeview.get_selection()
        model, iter = treeselection.get_selected()
        if not iter:
            return
        book = self.list_store.get_value(iter, 0)
        book.barcode = barcode
        book.author = author
        book.title = title
        self.update(book)
        self.list_store.set(iter, 1, barcode, 2, author, 3, title)

    def update(self, book):
        bookdboperation = getAdapter(book, IDbOperation)
        bookdboperation.update()

    def on_delete_clicked(self, *args):
        treeselection = self.treeview.get_selection()
        model, iter = treeselection.get_selected()
        if not iter:
            return
        book = self.list_store.get_value(iter, 0)
        self.delete(book)
        self.list_store.remove(iter)

    def delete(self, book):
        bookdboperation = getAdapter(book, IDbOperation)
        bookdboperation.delete()
    
catalogwindow = CatalogWindow()
