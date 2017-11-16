for file in $(ls Exercise11_files/Problem1/*.ref)
do
	file_name1=$(echo $file |  sed 's?^.*/??' | sed 's/.ref//')
	echo $file_name1
	/Analysis_Tools/Muscle.exe -in $file -out $file_name1.align 
done

for file in $(ls *.align)
do
	file_name2=$(echo $file | sed 's?^.*/??' | sed 's/.align//')
	echo $file_name2
	/Analysis_Tools/Hmmer/binaries/hmmbuild.exe $file_name2.hmmer $file
done

for file in $(ls *.align)
do
	rm $file
done

sigma=$(echo sigma.hmmer |  sed 's?^.*/??')
sporecoat=$(echo sporecoat.hmmer | sed 's?^.*/??')
transporter=$(echo transporter.hmmer | sed 's?^.*/??')
	
echo $sigma
echo $sporecoat
echo $transporter

for file in $(ls Exercise11_files/Problem1/*.fasta)
do	
	file_name3=$(echo $file | sed 's?^.*/??' | sed 's/.fasta//')
        echo $file_name3
	/Analysis_Tools/Hmmer/binaries/hmmsearch.exe --tblout $file_name3.sigma $sigma $file
	/Analysis_Tools/Hmmer/binaries/hmmsearch.exe --tblout $file_name3.transporter $transporter $file
	/Analysis_Tools/Hmmer/binaries/hmmsearch.exe --tblout $file_name3.sporecoat $sporecoat $file
done

for file in $(ls *.sigma)
do
	file_name4=$(echo $file | sed 's?^.*/??' | sed 's/.sigma//')
	cat $file | grep tr | tr -s ' ' | sed 's/ - / * /g' | cut -d " " -f2,3,5 | sed 's/*/'$file_name4'/g' >> temp.txt 	
done

for file in $(ls *.transporter)
do
        file_name4=$(echo $file | sed 's?^.*/??' | sed 's/.transporter//')
        cat $file | grep tr | tr -s ' ' | sed 's/ - / * /g' | cut -d " " -f2,3,5 | sed 's/*/'$file_name4'/g' >> temp.txt
done

for file in $(ls *.sporecoat)
do
        file_name4=$(echo $file | sed 's?^.*/??' | sed 's/.sporecoat//')
        cat $file | grep tr | tr -s ' ' | sed 's/ - / * /g' | cut -d " " -f2,3,5 | sed 's/*/'$file_name4'/g' >> temp.txt
done

cat temp.txt | grep -e sigma -e transporter -e sporecoat | sort -k1 > Results.txt

rm temp.txt
rm *.sigma
rm *.transporter
rm *.sporecoat
rm *.hmmer
