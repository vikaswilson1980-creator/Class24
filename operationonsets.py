#Different types of sets in python
mysets={1,2,3}
print(mysets)
#sets of mixed datatypes
myset={1.0,"Hello",(1,2,3)}
print(myset)
#sets cannot have duplicates
myset={1,2,3,4,3,2}
print(myset)
#we can make sets from the list
myset=set([1,2,3,2])
print(myset)
#remove a number from a set
numset=set([0,1,3,4,5])
print("The original set is",numset)
numset.pop()
print("After removing the first element from the set",numset)