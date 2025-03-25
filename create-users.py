#!/usr/bin/python3

# INET4031
# Steven Donath
# Date Created: 25 March 2025
# Date Last Modified: 25 March 2025

#os: Provides functions to run system commands and interact directly with the OS
#re: Provides regular expressions for pattern matching
#sys: Provides access to system parameters/functions like stdin for reading input
import os
import re
import sys

def main():
    for line in sys.stdin:

        #This regular expression searches for lines that start with a '#' (comment lines)
        match = re.match("^#",line)

        #This code removes whitespace and replaces it with a ':' to create a list where each element corresponds to a field
        fields = line.strip().split(':')

        #The if statement checks if the line is a comment (starts with '#') or if the number of fields does not equal 5. If so, it skips the line.
        if match or len(fields) != 5:
            continue

        # This code extracts the username, password, and full name from thee fields list
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Splits the code by commas to support multiple groups.
        groups = fields[4].split(',')

        #Prints message to confirm account creation for the username
        print("==> Creating account for %s..." % (username))
        #Command to add user with the provided detail (without setting a password)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #print cmd
        os.system(cmd)

        #Prints message to confiirm the password is being set for the user
        print("==> Setting the password for %s..." % (username))
        #Command to set the user's password using echo to input the password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #print cmd
        os.system(cmd)

        for group in groups:
            #If statement to check if the group is a placeholder with '-' character. If the group is valid, assigns the user to the group.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group) # Command to add the user to the group
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
