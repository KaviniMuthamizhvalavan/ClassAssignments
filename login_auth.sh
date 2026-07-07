username="admin"
password="Admin@123"

attempt=1


while [[ $attempt -lt 4 ]]
do
	if [[ $attempt -ne 1 ]]; then
		echo "$((4-attempt)) attempt left"
	fi
	
	echo 'Enter username: '
	read user
	echo 'Enter password: '
	read pwd

	if [[ $user == $username && $pwd == $password ]]; then
		echo "Login success"
		exit 1
		break
	else
		echo "Incorrect username or password"
		attempt=$((attempt+1))
	fi
done
echo "Too many failed attempts"
