1.
def idk(list):
    list.sort(reverse=True)
    return list

2.
def pp(l):
    res = []
    for i in l:
        if i % 2 == 0 and i !=0:
            res.append(i*2)
        else:
            res.append(i)
    print(res)

3.
def count(list,argument):
    res = 0
    for i in list:
        if i == argument:
            res += 1
    return res