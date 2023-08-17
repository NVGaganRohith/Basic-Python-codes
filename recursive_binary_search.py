def recursive_binary_search(list,target):
    if len(list)==0:
        return False
    else:
        mid=len(list)//2
        if list[mid]==target:
            return True
        elif list[mid]<target:
            return recursive_binary_search(list[mid+1:],target)
        else:
            return recursive_binary_search(list[:mid],target)
def verify(result):
    print("target found: ", result)
numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12]
result=recursive_binary_search(numbers,5)
verify(result)