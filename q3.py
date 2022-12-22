"""Write a Python program to create a list of tuples with the first element as the
number and Second element as the square of the number.
E.g. list = [3, 9, 10]
Output: [(3, 9), (9, 81), (10, 100)]"""
#input list
list1=list(map(int,input("Enter the numbers separated by space:").split()))
#blank list
list2=[]
for e in list1:
    t=(e,e*e)
    list2.append(t)
# Printing the final result
print("\nList containing (n,n^2) is shown below:")
print(list2)