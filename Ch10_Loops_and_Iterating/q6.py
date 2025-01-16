my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]
'''
new_list = []

for value in my_list:
    print(new_list)
    if value % 2 == 0:
        new_list.append("even")
    else:
        new_list.append("odd")

print(new_list)
'''

def evnod(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'

result = [evnod(num) for num in my_list]

print(result)

