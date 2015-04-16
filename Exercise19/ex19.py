# Exercise 19 - Function and Variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!") % cheese_count
    print("You have %d boxes_of_crackers!") % boxes_of_crackers
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def addition(n1,n2):
    sum = n1 + n2
    print("%d + %d = %d") % (n1,n2,sum)

n1=10;n2=10;
addition(1,1)
addition(1+2,1+2)
addition(n1,n2)
addition(n1+1,n2+2)
addition(n1+n1,n2+n2)
addition(1*2,1*2)
addition(n1*n2,n2*n1)
addition(1.0,2.0)
addition(n1-5,n2-5)
addition(50,50)
