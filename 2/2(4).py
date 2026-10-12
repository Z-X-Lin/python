s=input()
words=s.split( )
if"and"in words:
    i=words.index("and")
    words.insert(i,"anna")
    print(' '.join(words))
else:
    print("该行英文中没有”and”")