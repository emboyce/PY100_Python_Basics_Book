def remainders_5(numbers):
    return [number % 5 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

result = remainders_5(numbers_4)
print(result)
if any(rems == 0 for rems in result):
    print("Has numbers divisible by 5")
else: print("No numbers divisible by 5")

print(all([]))

