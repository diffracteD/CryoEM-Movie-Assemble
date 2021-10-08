#! /usr/bin/env python
######################################################################################################################
##################     File Copier (by walking nested directory)   #####################################################################
########################### v.1.0     (06/03/2020)          ##########################################################
###########################  Author: Abhisek Mondal, UCSF ############################################################
######################################################################################################################
"""
Program Description and input:
> Takes a parent directory path containing all *fractions.tiff (MOVIE) files
> Walks along the directory to search and analyze TIFF files
>Outputs:
    * copies all the matching extension files in a user provided directory


"""

import os
import sys
import itertools
from os.path import basename
from itertools import islice
import glob
import csv
import time
from shutil import copy

print "*********************************************************************************************************"
print "                  Hi there! You are executing EM MOVIE ASSEMBLE (EMA) algorithm on "+ time.asctime()+" PST "
print "                                     PROGRAM NAME: EM MOVIE ASSEMBLE (EMA) v.0.1 "
print "                                             designed by => Abhisek Mondal"
print "                                 abhisek.mondal@ucsf.edu[github:https://github.com/diffracteD]"
print "                                                 UCSF, California, USA"
print "**********************************************************************************************************"


path=raw_input("Please enter the SOURCE directory path containing all the *fractions.tiff files(Do Not enter / at the end of the path). . . \n ")
destinationDirectory=raw_input("Please enter the DESTINATION directory path where all files to be copied... \n")

count = 0 
#Starting to walk across directories of given path to open files
for root, dirs, files in os.walk(path):
    listOfFile = glob.iglob(os.path.join(root, '*fractions.tiff'))  #Getting all .gz files.
    print "          Enterring Directory: " + root

    
    for gzFileName in listOfFile:
        #Checking if target file is empty...
        if os.stat(gzFileName)[6] != 0: 
            #Trimming the path and keeping only the filename for cool output...
            filename = basename(gzFileName)
            
             
            
            #Generating header for the csv output..
            #maxOutHeader = str('File Name'), str('Max Peak'),str('volume/time'), str('intensity')
            #maxOutList.append(maxOutHeader)            
            
            #Opening and preparing .csv as per python array syatem...
            print " > Processing File: " + filename #shows current file being read...
            count += 1
            
            #Using shutil to copy files from nested directory to a particular direcroty...
            #Working syntax copy('source filename', 'destinaton directory')
            #Here 'gzFileName' will be used as source filename, bexause it gives the filename with full path.
            copy(gzFileName, destinationDirectory)
            
            
print ">> Total number of files copied: " + str(count)

print ">> Life is too short to go manual... Have a good one :) !!"
print "Peace out !!"
