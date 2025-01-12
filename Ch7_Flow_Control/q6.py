def may_cap(input):
    if len(input) > 10:
        return input.upper()
    else:
        return input
    
print(may_cap("hello"))
print(may_cap("dictionary11"))

