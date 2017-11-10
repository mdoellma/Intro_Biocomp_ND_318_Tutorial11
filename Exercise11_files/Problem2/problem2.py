#### Python script for #2 

#load packages
import re

#read in original fasta file
og_fasta=open("motifsort.fasta", "r")

#create the output files
motif1=open("motif1.fasta","w")
motif2=open("motif2.fasta","w")
motif3=open("motif3.fasta","w")

#loop over file
for Line in og_fasta:
    Line = Line.strip() #strip end of line
    if '>' in Line: # how can you tell if this is a sequence line?
        ID=Line # assign Line to ID
    else: 
        if re.search('AKKPRVZE', Line): 
            motif1.write(ID + "\n") 
            motif1.write(Line + "\n")
        elif re.search('AAQWWRNYGG', Line):
            motif2.write(ID + "\n") 
            motif2.write(Line + "\n")
        else: 
            motif3.write(ID + "\n") 
            motif3.write(Line + "\n")

#close files
og_fasta.close()
motif1.close()
motif2.close()
motif3.close()

