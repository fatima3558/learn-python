from sys import argv

script, filename = argv

file_obj = open(filename)

print(file_obj.read())

file_obj.close()