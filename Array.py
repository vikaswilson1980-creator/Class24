import array as arr
#create an array
arraynum=arr.array('i',[1,3,5,3,7,9,3])
print("The original array:"+str(arraynum))
#Count the number of occurrence
print("The number of occurrence of 3 in the said array is:"+str(arraynum.count(3)))
arraynum.reverse()
print("the reverse of the array of the items")
print(str(arraynum))