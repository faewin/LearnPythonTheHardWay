# Exercise 24 - More Practice

print "Let's practice everything."
# using \ as an escape character to rener ', newline and tab
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# """ is used to delimit the string below from line 9 to 14.
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

# performing arithmetic operations
five = 10 - 2 + 3 - 6

#using format string operator
print "This should be five: %s" % five

#creates function secret_formula which takes an Integer as an argument in this case. Then returns 3 values.
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

#argument for function above.
start_point = 10000
#return values from the function
beans, jars, crates = secret_formula(start_point)

#printing result of function:
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
