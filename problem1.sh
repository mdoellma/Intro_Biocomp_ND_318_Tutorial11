./muscle3.8.31_i86win32.exe -in ./tutorial/Intro_Biocomp_ND_318_Tutorial11/Exercise11_files/Problem1/sigma.ref -out ./tutorial/Intro_Biocomp_ND_318_Tutorial11/sigma.fasta

./muscle3.8.31_i86win32.exe -in ./tutorial/Intro_Biocomp_ND_318_Tutorial11/Exercise11_files/Problem1/sporecoat.ref -out ./tutorial/Intro_Biocomp_ND_318_Tutorial11/sporecoat.fasta

./muscle3.8.31_i86win32.exe -in ./tutorial/Intro_Biocomp_ND_318_Tutorial11/Exercise11_files/Problem1/transporter.ref -out ./tutorial/Intro_Biocomp_ND_318_Tutorial11/transporter.fasta

./hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe ./tutorial/Intro_Biocomp_ND_318_Tutorial11/sigma.hmm ./tutorial/Intro_Biocomp_ND_318_Tutorial11/sigma.fasta

./hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe ./tutorial/Intro_Biocomp_ND_318_Tutorial11/sporecoat.hmm ./tutorial/Intro_Biocomp_ND_318_Tutorial11/sporecoat.fasta

./hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe ./tutorial/Intro_Biocomp_ND_318_Tutorial11/transporter.hmm ./tutorial/Intro_Biocomp_ND_318_Tutorial11/transporter.fasta

for file in ./tutorial/Intro_Biocomp_ND_318_Tutorial11/Exercise11_files/Problem1/*.fasta
	do
		./hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $file.sigma.hit ./tutorial/Intro_Biocomp_ND_318_Tutorial11/sigma.hmm $file
		./hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $file.sporecoat.hit ./tutorial/Intro_Biocomp_ND_318_Tutorial11/sporecoat.hmm $file
		./hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $file.transporter.hit ./tutorial/Intro_Biocomp_ND_318_Tutorial11/transporter.hmm $file
	done
	
cat *.hit | grep -v "#" | awk '{print $1,$3,$5}' | sed -E 's/(tr)\|[0-9A-Z]+\|[0-9A-Z]+(_9)//g' >> output