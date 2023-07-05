def get_data():
    str1 = str(input("Enter the string : "))
    rev=""
    for i in range(len(str1)):
       rev=str1[i]+rev
    return rev
rev = get_data()
print("Rev : ",rev)