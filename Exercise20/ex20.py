# Exercise 20 - Functions and Files

#load module argv
from sys import argv

#declares script and inputfile to argv
script, input_file = argv

#function takes a file for input and prints the content
def print_all(f):
    print f.read()

#function takes a file for input and calls rewind to the beginning of file
def rewind(f):
    f.seek(0)

#function takes a line_count and file as an argument. Then prints specific line
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

#function is invoked
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#function is invoked
rewind(current_file)

print "Let's print three lines:"

current_line = 1
#function is invoked
print_a_line(current_line, current_file)

#function is invoked count in incremented
current_line += 1
print_a_line(current_line, current_file)

#function is invoked count in incremented
current_line += 1
print_a_line(current_line, current_file)
