  The purpose of the supplied software is to make it easy to access
  Sloan Digital Sky Survey (SDSS) data from Mathematica

  At present there is not really any error checking. It is hoped to add
  better error handling in the future

  Installation
  ============

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
        
  Ram Filing system
  =================

  Transfer between python and Mathematica takes place via temporary files
  to save wear and tear on your SD card setup a ram file system.

  I have made this 8 Megs, adjust to your requirements
    
     sudo mkdir /ram

     sudo nano /etc/fstab

     add the line
         tmpfs /ram tmps nodev,nosuid,size=8M 0 0 

     sudo mount -a

     df

   Checking SDSS is working
   ========================

   The following are useful to check SDSS is working

   http://cas.sdss.org/dr12/en/tools/quicklook/setId.asp?id=0x082802f0425a0031
   http://cas.sdss.org/dr12/en/tools/quicklook/quickobj.asp?id=588848900446814264

    Useful SQL Queries
    ==================
   
    http://cas.sdss.org/dr12/en/help/docs/realquery.aspx
 
    Mathematica Example NoteBooks
    =============================

    Example1.nb
      
    Retrieve a spectrum
    Plot the retrieved spectrum

    Example2.nb

    Run a sample SQL Query

    Mathematic Modules
    ==================

    The Mathematica Module is SDSS`.m and is initiated by calling

    Get["/home/pi/Mathematica/SDSS/SDSS`.m"] from Mathematica

    This makes the following functions available

    GetSpec["spectrum object id"]

    "Gets the CSV values for the spectrum object id"

    SQLQuery["SQL query"]

    "Performs the SQL query "SQL QUERY" and returns Column values as lists

    Python Scripts
    ==============

    The mathematica Modules makes use of some Python programs.

    These are

        sdss_getSpec.py

        "Retrieves a Spectrum"

        sdss_query.py
    
        "Performs an SQL Query"

    Linux scripts
    =============

    The following scripts test the function of the python scripts
    They are invoked without parameters

         testGetSpec
         testSimpleSelect
         testGetQSOs 

    Constructive feedback to
         
         keith@sloan-home.co.uk
