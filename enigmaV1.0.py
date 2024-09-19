ipt = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

r1 = {
    1:3,
    2:1,
    3:4,
    4:2,
}

r2 = {
    1:2,
    2:3,
    3:4,
    4:1,
}

r3 = {
    1:4,
    2:3,
    3:1,
    4:2,
}

minor = {
    1:1,
    2:4,
    3:2,
    4:3,
}

def enigma(a):
    pos = ipt.index(a)+1
    print(pos,"#1")
    fin = r1.get(pos)
    print(fin,"#2")
    fin = r2.get(fin)
    print(fin,"#3")
    fin = r3.get(fin)
    print(fin,"#4")
    fin = minor.get(fin)
    print(fin,"#5")
    fin = r3.get(pos)
    print(fin,"#6")
    fin = r2.get(fin)
    print(fin,"#7")
    fin = r1.get(fin)
    print(fin,"#8")
    res = ipt[fin-1]
    return res


a = input()
print(enigma(a))