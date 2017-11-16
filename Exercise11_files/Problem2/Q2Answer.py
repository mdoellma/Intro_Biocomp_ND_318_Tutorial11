#Q2
#Authors: Grant Keller and Kathleen Nicholson
# This code searches a .fasta file for specific motifs and places sequences containing
#  those motifs into files for each motif. 

#opens appropriate files
infile=open("motifsort.fasta","r")
outfile1=open("motif1.fasta", "w")
outfile2=open("motif2.fasta","w")
outfile3=open("neithermotif.fasta","w")

#assigns motifs as variables to use within the for loop
motif1="AKKPRVZE"
motif2="AAQWWRNYGG"
#for loop which loops over the motifsort.fasta file
for line in infile:
    #removes end of line characters
    line=line.strip()
    #recognizes lines with ">" and prints them in the appropriate outfile
    if line[0] == ">":
        ID=line
    #searches for each motif within each sequence. If found, prints to appropriate outfile.
    else:
        if motif1 in line:
            outfile1.write(ID + "\n")
            outfile1.write(line + "\n")
        elif motif2 in line:
            outfile2.write(ID + "\n")
            outfile2.write(line + "\n")
        else:
            outfile3.write(ID + "\n")
            outfile3.write(line + "\n")
        
#Closing files
infile.close()
outfile1.close()
outfile2.close()
outfile3.close()