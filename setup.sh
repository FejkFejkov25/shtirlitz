if [ ! -d ./venv/ ]; then
  printf "Virtual enviroment don't exist, creating this.\n"
  python3 -m venv venv
  [ $? -eq 0 ] && printf "Virtual enviroment created.\n" || printf "Virtual enviroment don't created.\n"
else
  printf "Virtual enviroment exist.\n"
fi

source ./venv/bin/activate
pip3 install -r requirements.txt

