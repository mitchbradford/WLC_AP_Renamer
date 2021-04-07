#!/usr/bin/env python
# Script by Mitch Bradford
# Dependencies - Netmiko, Python 3
# Instructions - list AP MAC Addresses, serial numbers and hostname in aps.csv

# -----------------------------------------------------------------------
import os.path

from datetime import datetime
from netmiko import ConnectHandler
from netmiko.ssh_exception import  NetMikoTimeoutException
from paramiko.ssh_exception import SSHException 
from netmiko.ssh_exception import  AuthenticationException
from getpass import getpass
from pprint import pprint
import csv
from banner import *

initial()			
main_menu()
script_mode = script_mode()

from ip_address import ip_address_of_wlc as ip_address_of_wlc

# -----------------------------------------------------------------------

username = input('Enter your username:')
password = getpass("Enter your password: ")
aps = csv.DictReader(open("aps.csv"))

# -----------------------------------------------------------------------

def rename_vwlc_devices(ip_of_wlc):
	"""
	Function using Netmiko to connect to the vWLC
	"""

	# Network device definition for Netmiko
	ios_device = {
	'device_type': 'cisco_ios',
	'ip': ip_address_of_wlc,
	'username': username,
	'password': password,
	}
	
	# Connect to device, run commands
	try:
		
		print ('Connecting to device ' + ip_address_of_wlc)
		remote_conn = ConnectHandler(**ios_device)
		
		# Run command to update hostname per AP in CSV
		for row in aps:
			remote_conn.send_command("config ap name " + row['hostname'] + " " + row['serial'])
			print("Updated device serial " + row['serial'] + " to " + row['hostname'])
		
		# Cleanly disconnect SSH session	
		remote_conn.disconnect()
		
	except IndexError as e:
		print("No line in the CSV:", e)
		pass

	except (AuthenticationException):
		print ('Authentication failure logging into device')
		
# -----------------------------------------------------------------------

def rename_c9800_devices(ip_of_wlc):
	"""
	Function using Netmiko to connect to the C9800 WLC
	"""

	# Network device definition for Netmiko
	ios_device = {
	'device_type': 'cisco_ios',
	'ip': ip_address_of_wlc,
	'username': username,
	'password': password,
	}
	
	# Connect to device, run commands
	try:
		
		print ('Connecting to device ' + ip_address_of_wlc)
		remote_conn = ConnectHandler(**ios_device)
			
		# C9800 command format is from enable, ap name <current name> name <new name>
		# new name format appears to be APxxxx.xxxx.xxxx

		for row in aps:
			remote_conn.send_command("ap name AP" + row['mac'] + " name " + row['hostname'])
			print("Updated device MAC " + row['mac'] + " to " + row['hostname'])
		
		# Cleanly disconnect SSH session	
		remote_conn.disconnect()
			
	except IndexError as e:
		print("No line in the CSV:", e)
		pass

	except (AuthenticationException):
		print ('Authentication failure logging into device')
		
def main():
	"""
	Call functions to run the script.
	Record the amount of time required to do this.
	"""
	start_time = datetime.now()

	# Run different commands based on the menu item selected
	if (script_mode == 1):
		print('Cisco vWLC')
		rename_vwlc_devices(ip_address_of_wlc)

	elif (script_mode == 2):
		print('Cisco C9800')
		rename_c9800_devices(ip_address_of_wlc)
		
	elif (script_mode == 3):
		print('This selection has not been implemented yet')
	elif (script_mode == 4):
		print('This selection has not been implemented yet')
	
	print("\nElapsed time: " + str(datetime.now() - start_time))

if __name__ == "__main__":
	main()
