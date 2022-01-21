import database
database.addrecord('ELLA', 'U', '22-05-2003','XYCadd' 'XYZ@GMAIL', 'xyz.com', 1234567)
# Deleting record requires you to use the rowid as a string here and not a int
# database.deleterecord('U')
# stuff = [('Bren', 'Gus', '01-01-2001', 'randomaddress', 'abc.com', 2345678), 
#     ('Den', 'Max', '02-02-2002', '2randaddress', 'bcd.com', 3456789)
# ]
# database.addmanyrecs(stuff)
# database.showAll()
database.email_adlookup("abc.com")
