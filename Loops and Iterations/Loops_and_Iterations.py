# Write a program which repeatedly reads numbers until the user enters "done".                      (DONE)
# Once "done" is entered, print out the total, count, and everage of the numbers.                   (DONE)
# If the user enters anything other than a number, detect their mistake using 'try' and 'except'    (DONE)
# Then Print an error message and skip to the next number                                           (DONE)
# (Re-write as definite loop after)                                                                 (DONE)

print('Enter as many numbers as you want, and I, Cortana, will calculate your results.')
print("Say 'Done' when you want the results processed.")


''' # How Lists Work #
num = list((input('Enter a number: ')))

numlist = [1, 2, 3]
list2 = list((1, 2, 3))

print(numlist)
print(list2)
print(num)
'''
       
Done = False       # Sets initial value so the program goes through at least once
numlist = []       # Blank list for filling values in

# ----------------------------------------------------------------------------------------------- #     Declaring stuff ^^^  Running stuff vvv
while Done is False:                      # Loops program (Until user enters 'Done' or 'done)
        print()
        num = input('Enter a value: ')   # Takes input from user
        try:                              # Checks if the input matches any of the correct values (Done, done, or any float/integer)
            if num == ('Done'):
                break                     # Breaks loop so user can go onto next step

            elif num == ('done'):         # Additional if statement for non capitalized 'Done'
                break

            elif float(num):               # Checks if input can be converted to a number (with negatives and/or decimals)
                numlist.append(num)        # Appends number inputted to number list
        except:                            # If number doesn't match required input, inform the user
            print('Invalid Character')
# ----------------------------------------------------------------------------------------------- # DO NOT TAMPER WITH, ABOVE CODE TAKES INPUT PROPERLY!!!
# Once "done" is entered, print out the total, count, and average of the numbers.  
numlistf = [float(x) for x in numlist]      # Converts list to float (VERY IMPORTANT)

sumlist = sum(numlistf)                      # Gets sum of number list
count = len(numlist)                        # Gets amount of numbers in number list
average = sumlist / count                   # Divides sum by number count to get mean average

total = ('Total: {}').format(sumlist)           # Formatting for end text
numnum = ('Number Count: {}').format(count)
avg = ('Average: {}').format(average)

print()
print(total)
print(numnum)
print(avg)
print()

input('-Press Enter to Exit-')  # Prevents program from closing, put at end of code

