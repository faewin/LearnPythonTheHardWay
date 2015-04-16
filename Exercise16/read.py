print "Below are the contents of your file"

from sys import argv

script, filename = argv

target = open(filename, 'r')
print target.read()
target.close()
