# Write a Python program to triple all numbers of a given list of integers. Use Python map.
number=[1,2,3,4,5,6,7]
print("The list before triple is:", number)
mapping =map(lambda x:x*3, number)
print("The triple of the list is:", list(mapping))
