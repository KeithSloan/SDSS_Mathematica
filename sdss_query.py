import sqlcl
import sys, os
from csvMathMod import csv2math

# Path for transfer files
prefix = "/ram/"
# prefix for transfer files
xfer = "xfer-"

if len(sys.argv) != 2 :
   print('Syntax is : python sdss_query.py "SQL query"')
   exit(0)
print("Executing Query : "+sys.argv[1]+"\n")

lines = sqlcl.query(sys.argv[1]).readlines()
# New versions seem to produce an extra first line with Table so remove
#print lines[1:]
os.system("rm "+prefix+xfer+"* 2> /dev/null")
csv2math(lines[1:])
