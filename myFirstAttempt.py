def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
attempts(5)



friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)


for n in range(0,11,2):
    print(n)
# This loop iterates on the value of the "n" variable in a range
# of 0 to 10 (the value of the end-of-range index 11 is excluded).
# The incremental value for the loop is 2. The print() function will
# output the resulting value of "n" as the loop counts from 0 to 10
# (end-of-range index 11) in incremental steps of 2. This is one
# method that can be used in Python to print a list of even numbers.