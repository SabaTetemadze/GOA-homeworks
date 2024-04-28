def find_last_even(number_list):
    for i in number_list:
        if i % 2 == 0:
            result = i
    print(result)


find_last_even([1,2,3,4,5])