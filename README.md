  The purpose of the supplied software is to make it easy to access
  Sloan Digital Sky Survey (SDSS) data from Mathematica

  At present there is not really any error checking. It is hoped to add
  better error handling in the future

## Installation

  Install prerequiste software

     sudo apt-get update
     sudo apt-get install git
     sudo apt-get install wget

     cd /home/pi/Mathematica

     git clone https://github.com/KeithSloan/SDSS_Mathematica.git SDSS

     Install sqlcl.py
     ----------------

     Either
        Download sqlcl.py from http://cas.sdss.org/dr12/en/help/download/sqlcl/ 
        to /home/pi/Mathematica/SDSS

     Or run
        GetSQLCL.sh

     Make executable
        chmod +x sqlcl.py
        
## Ram Filing system

  Transfer between python and Mathematica takes place via temporary files
  to save wear and tear on your SD card setup a ram file system.

  I have made this 8 Megs, adjust to your requirements
    
     sudo mkdir /ram

     sudo nano /etc/fstab

     add the line
         tmpfs /ram tmps nodev,nosuid,size=8M 0 0 

     sudo mount -a

     df

## Checking SDSS is working

   The following are useful to check SDSS is working

   http://cas.sdss.org/dr12/en/tools/quicklook/quicksummary.aspx?id=0x112d06c1a0530139&spec=0x0a2878485f006800

## Useful SQL Queries
   
   http://cas.sdss.org/dr12/en/help/docs/realquery.aspx
 
## Mathematica Example NoteBooks

    Example1.nb - Simple Select
    Example2.nb - Query to get Spectrum of QSO's
    Example3.nb - Retrieve a spectrum, Plot the retrieved spectrum

## Notes on Mathematica Variables

   Mathematica variables must begin with a lower case character
   so the first character of the returned SQL column is converted to
   lower case.

   Also underlines are not allowed in variables so these are removed. 

## Mathematic Modules

    The Mathematica Module is SDSS`.m and is initiated by calling

    Get["/home/pi/Mathematica/SDSS/SDSS`.m"] from Mathematica

    This makes the following functions available

    GetObjSpec["object id"]

    "Gets the CSV values for the object id"

    SQLQuery["SQL query"]

    "Performs the SQL query "SQL QUERY" and returns Column values as lists

    For details of SQL schema see

    http://cas.sdss.org/dr12/en/help/browser/browser.aspx

## Python Scripts

    The mathematica Modules makes use of some Python programs.

    These are

        "Retrieves a Spectrum"

        sdss-DR12_getSpec.py [specObjID]

        "Performs an SQL Query"
        
        sdss_query.py [query]

## Tailoring Python scripts

    To change the location where csv files are stored change
    the value of SpecPath in sdss-DR12_getSpec.py    

## Linux scripts

    The following scripts test the function of the python scripts
    They are invoked without parameters

         testGetSpecDR12
         testSimpleSelect
         testGetQSOs 

    Constructive feedback to
         
         keith@sloan-home.co.uk
