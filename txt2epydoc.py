#!/usr/bin/python

TXT_FILE = 'izca.txt'
SCRIPT_FILE = 'izca.py'

import sys
import doctest

txt = file(TXT_FILE)
script = doctest.script_from_examples(txt.read())
script_file = file(SCRIPT_FILE, 'w')
script_file.write(script)
script_file.close()

try:
    from epydoc import cli

except ImportError:
    print "================================="
    print "I can't find epydoc, it is required for %s" % sys.argv[0]
    print "You need to install epydoc to use this script"
    print "$ easy_install epydoc"
    print "should do it"
    sys.exit()  

sys.argv.append(SCRIPT_FILE)
cli.cli()
		 
print "================================="
print "Point your browser at html/index.html"
print "to see documentation for the code in %s" % TXT_FILE
