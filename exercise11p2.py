
#load packages

#open files to read and write
infile=open("/Users/Chloe/Desktop/data-shell/Intro_Biocomp_ND_318_Tutorial11/Problem2/motifsort.fasta","r")
outfile1=open("name","w")
outfile2=open("name","w")
outfile3=open("name","w")

outfile1.write("stuff to write" + "\n") so it doesn't write all on same line
outfile2.write("stuff to write" + "\n")
outfile3.write("stuff to write" + "\n")

#define variables
motif1="AKKPRVZE"
motif2="AAQWWRNYGG"


for line in infile
    line=line.strip()
    if line[0]==">": #header line
        ID=line
    else:
        if re.search(motif1, line): #re.search define motif1-2
            outfile1.write(ID + "\n")
            outfile1.write(line + "\n")
        elif re.search(motif2, line):
            outfile2.write(ID + "\n")
            outfile2.write(line + "\n")
        else:    
            outfile3.write(ID + "\n")
            outfile3.write(line + "\n")
            
infile.close()
outfile1.close()
outfile2.close()
outfile3.close()