========
ZCA Book
========

This repository contains reStructuredText source of ZCA book.


Files
-----

 - `default.css`: CSS imported from zope3.css (from Zope repository)

 - `zope3.css`: CSS files used for HTML rendering (from Zope
   repository)

 - `izca.txt`: Source of book

 - `rst2pdf.sh`: Script which combines commands for converting to HTML
   & PDF

 - `style.tex`: LaTeX stylesheet for PDF creation (from Grok
   repository)

 - `test_izca.py`: script for testing source (izca.txt is doctestable)


Creating HTML
-------------

To create HTML from izca.txt, first change this line::

  .. .. sectnum::

To::

  .. sectnum::

Then::

  rst2html --stylesheet=zope3.css izca.txt > zca.html

After creating HTML, change it back to original, otherwise contents
page in PDF output will be cluttered.


Creating PDF
------------

To create pdf just run the `rst2pdf.sh` script.  You should have
`pdflatex` and related TeX packages installed in your system.


Contributing to this project
----------------------------

If you would like to contribute to this project, just create a
personal bzr branch here: https://code.edge.launchpad.net/zcadoc

After you made any change in your branch, please inform me or Kent.
We will merge it to our branches and later we will publish it.

 - My Email Id: mbaiju AT muthukadan.net
 - Kent's Email Id: ktenney AT gmail.com


Guidelines
----------

 - Use double back-ticks (``) for: 

   - commands

   - directories

   - packages

   - modules

   - classes

   - functions

 - Use single back-tick (`) when you want to high-light some text.

 - Use two spaces after every sentence

 - Use maximum 70 characters per line

 - Skip two lines before chapters and sections

Regards,
Baiju M
http://www.muthukadan.net
