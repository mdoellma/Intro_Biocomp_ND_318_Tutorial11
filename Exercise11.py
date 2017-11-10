#import packages
import os
import numpy as np
import pandas as pd
import scipy
import sklearn
import scipy.integrate as spint
from plotnine import *
from ggplot import *
import matplotlib.pyplot as plt

#-------------------------------------PART 2---------------------------------------------

#set working directory
os.chdir('/Users/omneelay/Desktop/Exercise11/Intro_Biocomp_ND_318_Tutorial11/Exercise11_files/Problem2/')

#open read and write files
infile=open("motifsort.fasta",'r')
outfile1=open("motif1seqs",'w')
outfile2=open("motif2seqs",'w')
outfile3=open("otherseqs",'w')

#store regex as variables
motif1="AKKPRVZE"
motif2="AAQWWRNYGG"

#start of for loop
for line in infile:
    line=line.strip()
    #if header line, store ID
    if line[0]==">":
        ID=line
    else:
        #if motifs, store ID and seq to appropriate files
        if motif1 in line:
            outfile1.write(ID + "\n")
            outfile1.write(line + "\n")
        elif motif2 in line:
            outfile2.write(ID + "\n")
            outfile2.write(line + "\n")
        else:
            outfile3.write(ID + "\n")
            outfile3.write(line + "\n")

#close files
infile.close()
outfile1.close()
outfile2.close()
outfile3.close()