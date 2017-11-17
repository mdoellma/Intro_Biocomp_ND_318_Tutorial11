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

#notes
#We need to run the .fasta files through muscle to create the alignment files
#Then we can import the alignment files into Hmmer
#will input code below
#THIS IS A UNIX CODE SCRIPT

#create a list of the ref sequences to input these names into muscle
for file in *.ref
do
	echo $file | cut -d '.' -f1 >> ref_filenames.txt
done

#create a list of the fasta sequences to input these names into hmmsearch
for file in *.fasta
do
	echo $file | cut -d '.' -f1 >> fasta_filenames.txt
done

#for loop starts by looping through the ref files list of 3 (sigma, transporter, sporecoat)
for file in $(cat ref_filenames.txt)
do
    echo $file
#muscle alignment for the reference file in question
    muscle -in ${file}.ref -out ${file}.align
#hmmbuild from the muscle alignment to create .hmm file
    hmmbuild ${file}.hmm ${file}.align
#nested for loop (inside the above for loop) to loop through each organism for
#the hmm references created for each sequence feature of interest (the hmm refs that
#were created in the above for loop
for fasta in $(cat fasta_filenames.txt)
do
#create hmmsearch output in the format of refsequence_organism.hits with
#inputs refsequence.hmm and organism.fasta
    hmmsearch --tblout ${file}_${fasta}.hits ${file}.hmm ${fasta}.fasta
#display the results of the hmm serach, remove lines with #, and print columns of interest
#sed to change space delimiters to commas. Write to temp.txt file
    cat ${file}_${fasta}.hits | grep -v "#" | awk '{print $1, $3, $6}' | sed "s/ /,/g" > temp.txt
#loop through each line(match within the orgamism for the sequence) in temp.txt
for line in $(cat temp.txt)
do
#write to a new line in results.txt file in the format:
#organism,reference hammer search name (refsequence.hmm),three colums of info from above
    echo "${fasta},${file}.hmm",$line >> results.txt
done
rm temp.txt
done
done

    

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