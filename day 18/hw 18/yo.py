def otxis_jeradebi(z,x):
    res = []
    for i in range(z,x):
        if i % 4 == 0:
            res.append(i)
    return res




def saxeli_gvari():
    res = []
    s = input("enter tour name: ")
    g = input("enter your last name: ")
    res.append(s)
    res.append(g)
    return res



def aritmetikuli(list):
    z = 0
    for n in list:
        z += n
    v = len(list)
    s = z / v
    return s
