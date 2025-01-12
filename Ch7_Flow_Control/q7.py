def int_box(num):
    match num:
        case num if 0 <= num <= 50:
            print(f"{num} is between 0 and 50")
        case num if 51 <= num <= 100:
            print(f"{num} is between 51 and 100")


int_box(78)

