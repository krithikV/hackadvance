import os
comand = ['pkg install wget','wget https://github.com/Hax4us/TermuxBlack/raw/master/install.sh','chmod +x install.sh','./install.sh -i','apt update -y','apt upgrade -y','apt install curl','curl -LO https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh','chmod +x metasploit.sh','./metasploit.sh']
for i in comand:
    os.system(i)
