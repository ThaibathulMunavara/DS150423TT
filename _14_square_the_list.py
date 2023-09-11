list1 =[4,5,2,9]
def square(list1):
    return list1**2
result = list(map(square,list1))
print(result)