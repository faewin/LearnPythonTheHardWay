#creates variable formatter which holds 4 format characters
formatter = "%r %r %r %r"

#formatter takes 4 integers which prints => 1, 2, 3, 4
print formatter % (1, 2, 3, 4)
#formatter takes 4 string which prints => 'one', 'two', 'three', 'four'
print formatter % ("one", "two", "three", "four")
#formatter takes 4 booleans  which prints => True, False, False, True
print formatter % (True, False, False, True)
#formatter prints its string value 4 times.
print formatter % (formatter, formatter, formatter, formatter)
#formatter prints the string below
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
