info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
words = info.split(":")
print(words)
info_plus = "+".join(words)
print(info_plus)

# print("+".join(info.split(":")))

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
print(info.replace(":","+"))
