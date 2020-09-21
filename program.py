def Print_Even_Odd(arr):
    even_list=[]
    odd_list=[]
    for i in arr:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return f"Even Number is: {even_list}\n Odd Number is :{odd_list}"
print(Print_Even_Odd([i for i in range(1,51)]))