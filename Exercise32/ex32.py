# Example 32 - Loops and Lists

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through list
for number in the_count:
    print "This is the count %d" % number

#same as above
for fruit in fruits:
    print "A fruit type of %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r wince we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use range function to 0 to 5 counts
for i in range(0,6):
    print "Adding %d to list." % i
    # append function adds element to list
    elements.append(i)

# now we can print the list
for i in elements:
    print "Element was %d" % i
