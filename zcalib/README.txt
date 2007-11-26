ZCA based Library Management System
===================================

Note: This is a demo application, not for production use.

To run this application you will be required PyGTK, PySQLite and ZODB.

To run:

  python zcalib.py

Default storage is ZODB, to use relational database use `-r` switch:

  python dbschema.py (To populate DB schema, run only once)
  python zcalib.py -r

--
Baiju M

