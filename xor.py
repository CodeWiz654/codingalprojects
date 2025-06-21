a = int(input("Enter the first number:"))
b = int(input("Enter the seconde number:"))

if (a ^ b == 0):
    print("These numbers are equal")
else:
    print("These numbers ain't equal")


arr = [5,5,6,3,2,2,1,3,4,2]
result = 0
for num in arr:
    result = result ^ num


print("The numnber that appears an odd number os times is,", result)