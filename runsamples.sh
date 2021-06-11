g++ $1.cpp -o ./$1
echo "Compiled"

samples=`ls ./$1_input*.txt`
it=1

for sample in $samples
do
    echo "Sample $it"
    ./$1 < $sample > temp.txt
    diff $1_output$it.txt temp.txt
    echo # "\n"

    it=$((it+1))
done

echo "Finished"