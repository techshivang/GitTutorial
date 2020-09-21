def Print_Even_Odd(arr):
    even_list=[]
    odd_list=[]
    for i in arr:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list,odd_list
print(Print_Even_Odd([i for i in range(1,51)]))