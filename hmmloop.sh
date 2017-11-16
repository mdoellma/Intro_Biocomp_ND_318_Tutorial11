for i in *fasta
do
./hmmsearch --tblout $i.sigma.hits sigma.hmm $i
./hmmsearch --tblout $i.sporecoat.hits sporecoat.hmm $i
./hmmsearch --tblout $i.transporter.hits transporter.hmm $i
done

cat *.hits | grep "tr|" | sed -E 's/[tr|A-Z0-9]+\_9//' | awk '{print $1 " " $3 " " $5}' >hmmOut.txt

