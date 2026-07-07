mkdir day2_work
cd day2_work
touch file1.txt file2.txt file3.txt
echo "Day 2 class assignement" > file1.txt
cp file1.txt file2.txt
mv file2.txt file2_renamed.txt
mkdir new
mv file3.txt new/
find . -name "file1.txt"
touch script1.sh
echo "echo 'Hello'" > script1.sh
chmod 700 script1.sh
mkdir new2
tar -cvzf archive.tar.gz new2/
tar -xvzf archive.tar.gz -C new/
ls -l
