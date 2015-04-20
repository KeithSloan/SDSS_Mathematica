import sys, os
from csvMathMod import csv2math

# Path for where to save Spectrum CSV's
SpecPath = "/tmp/"
# Path of transfer files
prefix = "/ram/"
# transfer files prefix
xfer = "xfer-"

if len(sys.argv) != 2 :
   print('Syntax is : python sdss_getSpec.py "SpecObj"')
   exit(0)

spec = sys.argv[1]
print("Executing GetSpec : "+spec+"\n")

specOutFile = SpecPath+"spec-"+spec+".csv" 
cmd = "wget -o "+prefix+"trace -O "+specOutFile+" 'http://www.voservices.net/spectrum/search_details.aspx?format=csv&id=ivo%3A//jhu/sdss/dr6/spec/2.5%23"+spec+"'"
print cmd
os.system ( cmd )
lines = open(specOutFile,'r').readlines()
os.system("rm "+prefix+xfer+"* 2>/dev/null")
csv2math(lines)
