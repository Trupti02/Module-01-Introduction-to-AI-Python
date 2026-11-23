x = ["apple","banana","cherry","kiwi","mango"]
y = [43,23,41,26,86]

print(x)
print(y)

print("The first fruit in the list is", x[0]) # first element
z = x[0:3] # slicing
print(z) # printing fist 3 elements

x.sort()
print(x) #sort x

y.sort()
print(y) #sort y

x.extend(y) #join 2 list
print(x)

x.append("orange") # add new element
print(x)