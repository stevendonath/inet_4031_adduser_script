#!/usr/bin/python3

# INET4031
# Steven Donath
# Date Created: 25 March 2025
# Date Last Modified: 25 March 2025

# os: Provides functions to run system commands and interact directly with the OS
# re: Provides regular expressions for pattern matching
# sys: Provides access to system parameters/functions like stdin for reading input
import os
import re
import sys

def main():
    # Ask the user if they want to do a dry run
    dry_run = input("Would you like to perform a dry run (Y/N)? ").strip().lower()

    # Validate user input for dry-run prompt
    while dry_run not in ['y', 'n']:
        print("Invalid input. Please enter 'Y' for dry-run or 'N' for normal run.")
        dry_run = input("Would you like to perform a dry run (Y/N)? ").strip().lower()

    # Iterate over each line from stdin (input file)
    for line in sys.stdin:

        # Regular expression searches for lines that start with '#' (comment lines)
        match = re.match("^#", line)

        # Remove whitespace and split the line into fields using ':'
        fields = line.strip().split(':')

        # Skip lines that are comments or don't have exactly 5 fields
        if match or len(fields) != 5:
            if dry_run == 'y':
                print(f"Skipping invalid or comment line: {line.strip()}")
            continue

        # Extract the username, password, and full name from the fields
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split groups by commas to handle multiple groups
        groups = fields[4].split(',')

        # Print message for creating account (dry-run or normal execution)
        print(f"==> Creating account for {username}...")
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"

        if dry_run == 'y':
            print(f"Dry-run: {cmd}")  # Print the command instead of executing
        else:
            os.system(cmd)  # Execute the command in normal mode

        # Print message for setting the password
        print(f"==> Setting the password for {username}...")
        cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"

        if dry_run == 'y':
            print(f"Dry-run: {cmd}")  # Print the command instead of executing
        else:
            os.system(cmd)  # Execute the command in normal mode

        # Assign the user to groups
        for group in groups:
            if group != '-':
                print(f"==> Assigning {username} to the {group} group...")
                cmd = f"/usr/sbin/adduser {username} {group}"

                if dry_run == 'y':
                    print(f"Dry-run: {cmd}")  # Print the command instead of executing
                else:
                    os.system(cmd)  # Execute the command in normal mode

if __name__ == '__main__':
    main()
