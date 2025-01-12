def even_or_odd(num):
    # result = num % 2
    match num % 2:
        case 0:
            print("even")
        case _:
            print("odd")


even_or_odd(6)
even_or_odd(8)
even_or_odd(5)
even_or_odd(0)
