tup = (1, 2, 3, 4, 5)
tup = tup[(len(tup)-2):0:-1]
# print(tup)

tup2 = (1, 2, 3, 4, 5)
tup2 = list(tup2[1:len(tup2)-1])
tup2 = tuple(reversed(tup2))
# print(tup2)

tup3 = (1, 2, 3, 4, 5)
ltup3 = list(tup3)
ltup3.sort(reverse = True)
tup3 = tuple(ltup3[1:4])
print(tup3)


