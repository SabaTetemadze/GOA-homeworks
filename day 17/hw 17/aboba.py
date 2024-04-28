def shekreba(z):
    res = 0
    for i in z:
        res += i
    return res



def luwebi(list):
    list2 = []
    for a in list:
        if a % 2 == 0:
            list2.append(a)
    return list2


def didi(x):
        c = x[0]
        for b in x:
            if b > c:
                c = b
        return c
                  


def square(a):
    aa = []
    for i in a:
        aa.append(i*i)
    return aa



def ten(d):
    dd = []
    for i in d:
        if i > 10:
            dd.append(i)
    return dd