#Q2
#Authors: Grant Keller and Kathleen Nicholson

infile=open("motifsort.fasta","r")
outfile1=open("motif1.fasta", "w")
outfile2=open("motif2.fasta","w")
outfile3=open("neithermotif.fasta","w")

motif1="AKKPRVZE"
motif2="AAQWWRNYGG"
#Q2 code
for line in infile:
    line=line.strip()
    if line[0] == ">":
        ID=line
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