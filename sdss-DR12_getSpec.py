import sys, os
from csvMathMod import csv2math

# Path for where to save Spectrum CSV's
SpecPath = "/tmp/"
# Path of transfer files
prefix = "/ram/"
# transfer files prefix
xfer = "xfer-"

#print "Args : "
#print len(sys.argv)
if len(sys.argv) != 6 :
   print('Syntax is : python sdss_getSpec.py "ObjID","plate","mjd","fiber","reduction2d"')
   exit(0)

spec = sys.argv[1]
plate = sys.argv[2]
mjd = sys.argv[3]
fiber = sys.argv[4]
reduction = sys.argv[5]
print("Executing GetSpec : "+spec+"\n")

specOutFile = SpecPath+"spec-"+spec+".csv" 
cmd = "wget -o "+prefix+"trace -O "+specOutFile+" 'http://dr12.sdss3.org/csvSpectrum?plateid="+plate+"&mjd="+mjd+"&fiber="+fiber+"&reduction2d="+reduction+"'"
print cmd
os.system ( cmd )
lines = open(specOutFile,'r').readlines()
os.system("rm "+prefix+xfer+"* 2>/dev/null")
csv2math(lines)
