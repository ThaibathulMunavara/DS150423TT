
length = int(input("Enter the length of list : "))
tuples = []
for i in range(length):
  no =input("Enter the list of tuples : ").split()
  tuples.append(tuple(map(int,no))) 
print("  Tuples of list      : ",tuples)
sorted_tuples=[]
for i in tuples:
  sorted_tuples.append((i[0],i[-1]))
sorted_tuples = sorted(sorted_tuples, key=lambda x: x[-1]) #lambda argument : expression
print("Sorted list of tuples : ",sorted_tuples)

