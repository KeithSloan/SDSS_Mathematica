import sys, os
from csvMathMod import csv2math

if len(sys.argv) != 2 :
   print('Syntax is : csv2math <csv_file>')
   exit(0)

csvFile = sys.argv[1]
print("Executing csv2math : "+csvFile+"\n")
lines = open(csvFile,'r' ).readlines()
#print lines
csv2math(lines)
