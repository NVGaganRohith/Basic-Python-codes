new_list=[1,2,3] #lists act similar to arrays
result=new_list[0] #refer to elements via index
if 1 in new_list: print(True) #checks if element present in the list
new_list.append(89) 
# The append happens after python uses resize function which chnages list size from 0,4,8,16,25,35,46
# has constant time complextiy despite the fact that memory allocation is increasing randomly because avarage remains constant
print(new_list)
numbers=[4,5,6]
new_list.extend(numbers)# O(k) time complexity 
print(new_list)