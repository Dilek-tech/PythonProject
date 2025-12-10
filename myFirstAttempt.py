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


for n in range(0,11,2):                    # The loop should print 0, 2, 4, 6, 8, 10
    print(n)



for number in range(2,7+1):               # The loop should print 6, 9, 12, 15, 18, 21
    print(number*3)




for x in range(2, -2, -1):                # The loop should print 2, 1, 0, -1
    print(x)


    def sum_positive_numbers(n):
        # The base case is n being smaller than 1
        if n < 1:
            return 0

        # The recursive case is adding this number to
        # the sum of the numbers smaller than this one.
        return n + sum_positive_numbers(n - 1)


    print(sum_positive_numbers(3))  # Should be 6
    print(sum_positive_numbers(5))  # Should be 15


   # def recursive_function(parameters):
#    if base_case_condition(parameters):
   #         return base_case_value
    #    recursive_function(modified_parameters)


