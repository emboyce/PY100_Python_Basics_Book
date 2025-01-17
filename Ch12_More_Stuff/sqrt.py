# Eliza's stab at a simple square-root function for integers
# I first tried to generate a random integer but this doesn't work because they don't all have integer squares
# This has better run-time than just testing all the integers below num, but I think it could be improved
# It does not have better results than starting at 1 and counting up!
# Some sort of sort-like method of norrowing down ranges

''' Testing Random

import random

max_num = 10
i = 0

while i < 10:
    num = random.randint(1, max_num)
    print(num)
    i += 1
'''

count = 1
num = 1296
print(f"Number is {num}")


low_num = 0
high_num = int(num / 2 ) + 1
#Test num divided by 2, rounded up - this is the highest int it could be
test_num = high_num
low_list = [test_num]
high_list = [test_num]
while True:
    print(f"Test is {test_num}")
    product = test_num * test_num
    print(f"Product is {product}")
    if product == num:
        print(f"{test_num} is sqrt")
        print(f"Total iterations were {count}")
        print(low_list, high_list)
        break
    elif product > num:
        # test_num is too high
        # go to the bottom of the current range
        low_num += 1
        test_num = low_num
        low_list.append(low_num)
    elif product < num:
        #test_num is too low
        #go to the top of the current range
        high_num -= 1
        test_num = high_num
        high_list.append(high_num)
    
    count += 1


    