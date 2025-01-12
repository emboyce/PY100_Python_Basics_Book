stuff = ('hello', 'world', 'bye', 'now')

stuff = list(stuff)
stuff[2] = "good" + stuff[2]
stuff = tuple(stuff)
print(stuff[2])
