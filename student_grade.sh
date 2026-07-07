echo "Enter mark 1: "
read mark1
echo "Enter mark 2: "
read mark2
echo "Enter mark 3: "
read mark3
echo "Enter mark 4: "
read mark4
echo "Enter mark 5: "
read mark5

total=$((mark1+mark2+mark3+mark4+mark5))
echo "Total marks ${total}"

avg=$((total/5))

echo "Average marks ${avg}"

if [[ $avg -ge 90 ]]; then
	grade=A
elif [[ $avg -ge 75 ]]; then
	grade=B
elif [[ $avg -ge 60 ]]; then
	grade=C
elif [[ $avg -ge 50 ]]; then
	grade=D
else
	grade="Fail"
fi

echo "Your grade is ${grade}"
