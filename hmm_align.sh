for file in $(ls Exercise11_files/Problem1/*.ref)
do
	file_name=$(echo $file |  sed 's?^.*/??' | sed 's/.ref//')
	echo $file_name
done
