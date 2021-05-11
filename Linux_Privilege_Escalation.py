#!/usr/bin/env python3 

# Linux Privilege Escalation Script!

import os

# Scan for OS, Release, and Kernel info
def OS_KERNEL_SCAN():
	if clock != 0:
		os.system('uname -a')   # This will run the 'uname -a' command
		os.system('cat /etc/os-release')
		os.system('cat /etc/issue')
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("")
		ROOT_SERVICE_SCAN()
	else:	 
		os.system('uname -a')   
		os.system('cat /etc/os-release')
		os.system('cat /etc/issue')
		GOTOMAIN = input("Press ENTER to return to MAIN function.")
		MAIN()
	
# Applications & Services
# Scan for services running as root
def ROOT_SERVICE_SCAN():
	if clock != 0:
		print("Applications & Services running as root:")
		os.system('ps aux | grep root')
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("")
		SUID_GUID_SCAN()
	else:	
		print("Applications & Services running as root:")
		os.system('ps aux | grep root')
		GOTOMAIN = input("Press ENTER to return to MAIN function.")
		MAIN()
	
# Scan for abusable SUID/GUID binaries
def SUID_GUID_SCAN():
	if clock != 0:
		print("***SUID/GUID SCAN***")
		print("")
		print("---SUID SCAN---")
		os.system('find / -perm -u=s -type f 2>/dev/null')   # SUID (chmod 4000) - run as the owner, not the user who started it.
		print("")
		print("---GUID SCAN---")
		os.system('find / -perm -g=s -type f 2>/dev/null')   # SGID (chmod 2000) - run as the group, not the user who started it.
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("")
		GOTOMAIN = input("Full Scan Succeed!!! Press ENTER to return to MAIN function.")
		MAIN()
	else:
		print("***SUID/GUID SCAN***")
		print("")
		print("---SUID SCAN---")
		os.system('find / -perm -u=s -type f 2>/dev/null')
		print("")
		print("---GUID SCAN---")
		os.system('find / -perm -g=s -type f 2>/dev/null')
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("")
		GOTOMAIN = input("Press ENTER to return to MAIN function.")
		MAIN()
	

def MAIN():
	#os.system('clear')  It will clear the screen.
	global clock
	clock = 0
	OPTION = input("""
		1) Scan OS/Kernel 
		2) Scan Root Service 
		3) Scan SUID/GUID 
		4) Run All Scan
		5) EXIT

		>>>""")

	print("Use: " + OPTION)
	if OPTION == "1":
		OS_KERNEL_SCAN()

	elif OPTION == "2":
		ROOT_SERVICE_SCAN()

	elif OPTION == "3":
		SUID_GUID_SCAN()

	elif OPTION == "4":
		clock = clock + 1
		OS_KERNEL_SCAN()	

	elif OPTION == "5":
		exit()	

	else:
		WRONG_OPTION = input("Invalid option. Press ENTER to continue.")	
		MAIN()
			

MAIN()
