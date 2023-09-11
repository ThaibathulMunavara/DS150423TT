list1 = [1,2,3,4,5,6,7]
def triple(n):
    return n*3
result = list(map(triple,list1))
print(result)