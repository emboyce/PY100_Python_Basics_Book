my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)


def find_integers(tup):
    int_list = []
    for element in tup:
#       if type(element).__name__ == "int":
        if type(element) is int:
            int_list.append(element)
    return int_list


integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]