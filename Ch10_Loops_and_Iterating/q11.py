my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

out_index = 0
while out_index < len(my_list):
    #print(my_list[out_index])
    in_index = 0
    #print(my_list[out_index][in_index])
    while in_index < len(my_list[out_index]):
        if my_list[out_index][in_index] % 2 == 0:
            print(my_list[out_index][in_index])
        in_index += 1
    out_index += 1

    