# INET 4031 Add Users Script and User List 

## Program Description

The Add Users Script automates the process of creating new users on an Ubuntu system. Typically a sysadmin must manually execute a series of commands to add a user, such as 'adduser', 'passwd', and 'adduser <username> <group>' for each individual user. These commands require specific information for the user's account like username, password, and full name, but automates the process by reading this information from an input file and executing the sequence of commands. This allows the sysadmin to quickly create/configure multiple users with minimal effort.


The script reads an input file containing the relevant user info and then processes each line before executing the sequence of commands to: 
1. Create the user account using 'adduser'
2. Set the user password using 'passwd'
3. Assign the user to specific groups

## Program User Operation

To run the program, provide the input file in the specific format, including details such as username, password, full name, and groups. Then execute the script on the command line using ./create-users.py < create-users.input
Before running the script, ensure that the Python script is executable by running chmod +x create-users.py

## Input File Focreate

These fields include:

1. **Username**: username for new user account
2. **Password**: password for new user account
3. **Last Name**: last name of the user 
4. **First Name**: first name of the user 
5. **Groups**: separated by commas, a list of groups the user should be added to

Example input file:

user01:pass01:Last01:First01:group01
user02:pass02:Last02:First02:group01,group02
user03:pass03:Last03:First03:-

To skip a line, prefix the line with # to designate it as a comment. The script will ignore any commented lines or lines that do not contain exactly 5 fields.
If you do not wish to add a new user to any groups, ensure the fifth field contains the '-' character.


## Command Execution 

Before running the script, ensure that the Python script is executable by running chmod +x create-uers.py prior to running ./create-users.py < create-users.input to execute the code.

## Dry Run

To run the script without having an effect on the system and to test the code, ensure that all os.system(cmd) lines are COMMENTED OUT. Otherwise, these commands will be ran by the system and executed. This allows for testing and ensuring everything is set up correctly prior to making important changes. 
