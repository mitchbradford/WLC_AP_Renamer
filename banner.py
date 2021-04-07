# -----------------------------------------------------------------------
"""
ASCII art banner and selection menu for the script
"""
def initial():
	print('')
	print('==========================================================')
	print(' _____ _                 _    _ _     _____             ')
	print('/  __ (_)               | |  | | |   /  __ \            ')
	print('| /  \/_ ___  ___ ___   | |  | | |   | /  \/            ')
	print('| |   | / __|/ __/ _ \  | |/\| | |   | |                ')
	print('| \__/\ \__ \ (_| (_) | \  /\  / |___| \__/\            ')
	print(' \____/_|___/\___\___/   \/  \/\_____/\____/            ') 
	print('                                                        ')
	print('                                                        ')
	print('  ___        _                        _   _             ')
	print(' / _ \      | |                      | | (_)            ')
	print('/ /_\ \_   _| |_ ___  _ __ ___   __ _| |_ _  ___  _ __  ')
	print("|  _  | | | | __/ _ \| '_ ` _ \ / _` | __| |/ _ \| '_ \ ")
	print('| | | | |_| | || (_) | | | | | | (_| | |_| | (_) | | | |')
	print('\_| |_/\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___/|_| |_|')
	print('                                                        ')
	print('==========================================================')
	print ('')
	print ('This script will bulk rename APs on a Cisco vWLC or C9800')
	print ('based on the menu item selected.')

def main_menu():
	print ()
	print ('What is the model of the Cisco WLC:')
	print ()
	print ('1 - Cisco vWLC')
	print ('2 - Cisco C9800')
	print ('5 - Exit')
	print ()

def script_mode():
	while True:
		try:
			prompt = 'Your selection: '
			selection = int(eval(input(prompt)))
			print('')
		except:
			print ('Invalid option. Please enter 1-5.')
			main_menu()
		else:
			if selection == 1:
				return selection
			elif selection == 2:
				return selection
			elif selection == 5:
				exit()
			else:
				print ('Invalid option. Please enter 1-5.')

# -----------------------------------------------------------------------