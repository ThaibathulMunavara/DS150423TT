def get_info():
    str1=str(input("Enter the string: "))
    lower=0
    upper=0
    for i in str1:
        if i.isupper():
           upper+=1
        elif i.islower():
            lower+=1
    return upper,lower
upper,lower =get_info()
print("No of Upper case characters : ",upper)
print("No of Lower case characters : ",lower)
        