#O(n)
def linear_search(list, target):
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if (index!=None):
        print("Target index is: ", index)
    else:
        print("Target not found")
numbers=[1,2,3,4,5,6,7,8,9]
result= linear_search(numbers,6)
verify(result)