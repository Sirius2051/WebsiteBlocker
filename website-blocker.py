#!/usr/bin/python
#
# You need run the script as root.
#
# Import the module 'os' to consult the operating system that we are using.
#
import os
#
# Make the query mentioned in the comment above and save it in a variable for later use.
#
os_name = os.name
#
# Print a welcome message to the user on the screen. The text is painted orange.
#
print('\033[;33m'+'Enter a URL or write \'ok\' to close the program.')
#
# Create an empty list in which the websites that the user will enter.
#
websites_list = []
#
# Define the 'input_control()' function.
# Controls data entry to store in the list created for websites that the user wants to block.
# It also allows you to exit the process by typing 'ok'.
# The information entered by the user will be painted purple.
#
def input_control():
    qwerty = input('\033[;35m'+'\t')
    if qwerty == 'ok':
        pass
    else:
        websites_list.append(qwerty)
        input_control() 
#
# Start the execution of the function 'input_control()'.
#
input_control()
#
# Define function 'blocker()'.
# This function will open the 'hosts' file and write to it the introduced websites
# to redirect to the 'localhost' every time you try to access any of them.
# The receiving parameter will allow you to pass the location of the 'hosts' file taking into account the operating system.
#
def blocker(route):
    with open(route, 'r+') as file:
        content = file.read()
        for website in websites_list:
            if website in content:
                pass
            else:
                line = '127.0.0.1 \t'+website+'\n'
                file.write(line)
#
# Checking the operating system and based on that we pass the path to the 'blocker()' function to execute the website blocking.
#
if os_name == 'posix':
    route = '/etc/hosts'
    blocker(route)
elif os_name == 'nt':
    route = 'C:\Windows\System32\drivers\etc\hosts';
    blocker(route)
else:
    print('\033[;31m'+'Your operating system is not supported. Please contact us.')
#
# Print a farewell message that indicates the status of the operations.
#
if len(websites_list) > 0:
    print('\033[;32m'+'Operations successfully completed.')
else:
    print('\033[;31m'+'You have not indicated any website.')
