# Exercise 15 - Reading Files

#loads argv module
from sys import argv
#we ask python to load 2 arguments script, and text file
script, filename = argv
#we ask python to open the text file
txt = open(filename)

#print statement with filename
print "Here's your file %r:" % filename
#we call the read method wich prints the lines from thefile
print txt.read()
#close text file
txt.close()

#Repeat...
#print "Type the filename again:"
#file_again = raw_input("> ")
#txt_again = open(file_again)

#print txt_again.read()
