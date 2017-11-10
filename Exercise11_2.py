import re
import numpy
import pandas

master=open('motifsort.fasta','r')
m1=open('motif1.fasta','w')
m2=open('motif2.fasta','w')
ee=open('everythingelse.fasta','w')


motif1=r'AKKPRVZE'
motif2='AAQWWRNYGG'

for line in master:
    line=line.strip()
    if > not in line:
        if motif1 in line:
            m1.write('')


master.close()
m1.close()
m2.close()
ee.close()
    
