def merge_sort(list):
    """
    Sort in an ascending order
    returns a new sorted list

    Divide : find midpoint of list and divide into sublists
    conquer: Recursivelysort the sublits created in the previous steps
    Combine: merge the sorted sublists created in the previous step
    takes overall O(kn log n)

    if split function is remodelled then time complexity would be O(n log n)
    Takes O(N) space complexity
    """
    if(len(list)<=1):
        return list
    left_half,right_half = split(list)
    left=merge_sort(left_half)
    right=merge_sort(right_half)
    return merge(left, right)

def split(list):
    """Divide the unsorted list at midpoint into sublists returns two sublists left and right, Takes overall O(k log n) k because the python slicing function has O(k) time complexity"""
    mid=len(list)//2
    left=list[:mid]
    right=list[mid:]
    return left,right
def merge(left,right):
    """Merges two lists(arrays), sorting them in the process returns a new merged list, Runs in overall O(n log n) n for merge and long n for splitting"""
    l=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            l.append(left[i])
            i=i+1
        else:
            l.append(right[j])
            j=j+1
    while i<len(left):
        l.append(left[i])
        i=i+1
    while j<len(right):
        l.append(right[j])
        j=j+1
    return l
def verify_sorted(list):
    n=len(list)
    if n==0 or n==1:
        return True
    return list[0]<=list[1] and verify_sorted(list[1:])
alist=[54,26,62,93,17,77,31,54,78,9,2,45]
l=merge_sort(alist)
print(l)
print(verify_sorted(alist))
print(verify_sorted(l))