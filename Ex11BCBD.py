##Number 2##

#load packages
import pandas
import re

#Open files to read and write
infile = open("motifsort.fasta","r")
outfile1 = open("motif1.txt","w")
outfile2 = open("motif2.txt","w")
outfile3 = open("nomatch.txt","w")

#assign regex to variable name, or compile to variable name

motif2=r"(AAQWWRNYGG)"
motif1=r"(AKKPRVZE)"

#loop over file #look at old code to see how you looped over a file
for Line in infile:
    #strip end of line
    Line = Line.strip()
    
    #if motif 1
    #how can you tell if this is the header line?
    if Line[0]==">":
        ID=Line
    else:
        if re.search(motif1,Line): 
        #write unchanged header line to file
            outfile1.write(ID + "\n")
            outfile1.write(Line + "\n")
    
        #if motif 2:
        elif re.search(motif2,Line):
            outfile2.write(ID + "\n")
            outfile2.write(Line + "\n")
    
        #if no match
        else:
            outfile3.write(ID + "\n")
            outfile3.write(Line + "\n")

#Close files
infile.close()
outfile1.close()
outfile2.close()
outfile3.close()

