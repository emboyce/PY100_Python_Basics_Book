age = int(input("What is your age? "))
years = range(10, 50, 10)
print(years)
for i in years:
    print(i)
    print(f"In {i} years, you will be {age + i} years old.")

