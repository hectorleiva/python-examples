# The Fizz Buzz problem
# Ok, starting with the number 1, start counting up to 100 print the numbers
# BUT - for every number that is divisible by 3, instead print "Fizz" in its place
# ALSO - for every number that is divisible by 5, instead print "Buzz" in its place
# AND YEAH AND - for every number that is divisible by both 3 AND 5, print "FizzBuzz" together

for count in range(1, 101):
    if ((count % 5) is 0) and ((count % 3) is 0):
        print "FizzBuzz"
    elif not(count % 3):
        print "Fizz"
    elif not(count % 5):
        print "Buzz"
    else:
        print count
