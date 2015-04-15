#creates variable x then assigns witht the value of the statement then substitutes the format character %d with 10
x = "There are %d different type of people." % 10
#creates variable binary which holds the value of string 'binary'
binary = 'binary'
#creates variable do_not which holds the value of string "don't"
do_not = "don't"
#creates variable y then assigns witht the value of the statement then substitutes the format character %s with binary and do_not
y = "Those who know %s and those who %s" % (binary, do_not)
#prints the value of the variable
print x
#prints the value of the variable
print y
#note to self %r is used for debugging purposes, simalar to 'p' in ruby.

#prints statement and substitutes the format character %r with value of value of x
print "I said: %r." % x
#prints statement and substitutes the format character %s with value of value of y
print "I also said: '%s'." % y
#creates variable halarious which holds the boolean value of False
hilarious = False
#creates variable joke_evaluation which holds a string value and format character
joke_evaluation = "Isn't this joke so funny?! %r"
#prints statment and substitutes the format character %r with the value of halarious.
print joke_evaluation % hilarious
#create variable w which holds a string as a value
w = "This is the left side of..."
#create variable w which holds a string as a value
e = "a string with a right side."
#concatinates variable w, with variable e
print w + e
