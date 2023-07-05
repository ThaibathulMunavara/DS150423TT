def _get_info():
    length =int(input("Enter the size of list: "))
    list=[]
    for i in range(length):
        no=int(input("Enter the Number : "))
        list.append(no)
    return list
def _calculation(list):
    sum=0
    for i in list:
        sum+=i
    print("Sum : ",sum)

list =_get_info()
print("List : ",list)
_calculation(list)