# Exercise 32 - While loops

def method(max_num, inc):
    i = 0
    numbers = []

    for i in range(0,max_num):
        pass
        print "At the top i is %d" % i
        numbers.append(i)

        i += inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "
    for num in numbers:
            print num

method(6,1)
