my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

dict = {keys:len(keys) 
        for keys in my_set 
        if len(keys) % 2 != 0}

print(dict)

