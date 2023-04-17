from array import *
a = [["saimon", "mahi", "mohan", "aopu", "rashel", "kaniz"], ["alu", "begun", "porota", "shim", "kola"],
     ["balu", "kalu", "chalu"]]
a.append(2, ["alu","kalu", "chalu"])
for r in a:
    for c in r:
        print(c, end=" ")
    print()
