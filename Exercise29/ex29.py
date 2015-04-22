#Exercise 29 - What if

people = 20
cats = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"


dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."


if people == dogs:
    print "People are dogs."


#What do you think the if does to the code under it?
# The code will execute if the block yields true
#Why does the code under the if need to be indented four spaces?
# It's pythons way of seperating another block of code.
#What happens if it isn't indented?
# Python Indentation Error
#Can you put other boolean expressions from Exercise 27 in the if-statement? Try it.
# Yes you can.
#What happens if you change the initial values for people, cats, and dogs?
# The results will vary depending if it's a truthy or falsey.
