import os
comand = ['pkg install wget','wget https://github.com/Hax4us/TermuxBlack/raw/master/install.sh','chmod +x install.sh','./install.sh -i','apt update -y','apt upgrade -y','apt install curl','curl -LO https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh','chmod +x metasploit.sh','./metasploit.sh','pkg install apache2','apachectl -k start','rm /data/data/com.termux/files/usr/share/apache2/default-site/htdocs/index.html','mv payload.py /data/data/com.termux/files/usr/share/apache2/default-site/htdocs']
for i in comand:
    os.system(i)
