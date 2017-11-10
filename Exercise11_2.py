import re
import numpy
import pandas

#Load files
master_in = open('motifsort.fasta','r')
m1_out = open('motif1.fasta','w')
m2_out = open('motif2.fasta','w')
misc_out = open('misc_motif.fasta','w')

#define patterns
motif1=r'AKKPRVZE'
motif2=r'AAQWWRNYGG'

#loop line by line
for line in master_in:
    line=line.strip()
    #Define ID
    if (line[0] == ">"):
        ID = line
    else (">" not in line):
        #add to out files based on presence of certain motif
        if (re.search(motif1, line)):
            m1_out.write(ID + "\n")
            m1_out.write(line + "\n")
        
        elif (re.search(motif2, line)):
            m2_out.write(ID + "\n")
            m2_out.write(line + "\n")
        else:
            misc_out.write(ID + "\n")
            misc_out.write(line + "\n")

#close all files
master_in.close()
m1_out.close()
m2_out.close()
misc_out.close()
    
