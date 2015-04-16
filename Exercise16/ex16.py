# Excercise 16 - Reading and Writing Files

# load module argv and ask for filename and script.
from sys import argv
script, filename = argv

# asking user if he wants to proceed
print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

#opens filename in write mode
print "Opening the file..."
target = open(filename, 'w')

# truncate emptys the file.
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#refactored
output = "%s\n%s\n%s\n" %(line1,line2,line3)
target.writelines(output)

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, we close it."
target.close()

