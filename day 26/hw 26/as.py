def manual_sum(list):
    res = 0
    for i in list:
        res += i
    print(res)

def manual_max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    print(max)

def manual_min(list):
    min = list[0]
    for i in list:
        if i < min:
            max = i
    print(min)

def manual_len(list):
    print(len(list))

def manual_reduce(list):
    fake = []
    for i in list:
        fake.append(i)
    print(fake)
    print(list)