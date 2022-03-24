# this imports `argv` from the `sys` standard library module
from sys import argv

# unpacks the 2 pieces of info we get from `argv`:
# the name of this script && the name of the file
# we pass in as an argument
script, filename = argv

# this opens the file and stores a file-type obj in `txt`
txt = open(filename)

# this prints the name of the file we passed in...
print(f"Here's your file {filename}:")
# and this prints its contents
print(txt.read())

# this prints a string
print("Type the filename again:")
# this is the input prompt; user input gets stored as
# `file_again`
file_again = input("> ")

# this opens the file from the name the user input &
# stores it as a file-type obj in `txt_again`
txt_again = open(file_again)

# prints contents of file
print(txt_again.read())

txt.close()
txt_again.close()