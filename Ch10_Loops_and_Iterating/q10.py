import random

highest = 10

def get_number(top_range):
    number = random.randrange(top_range + 1)
    print(number)
    return number

number = get_number(highest)


while number != highest:
    number = get_number(highest)
