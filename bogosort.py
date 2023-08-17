import random
numbers = [3,6,8,7,4,2,1]
def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True

def bogo_sort(values):
    attempt=0
    while not is_sorted(values):
        random.shuffle(values)
        attempt+=1
    print(attempt)
    return values
print(bogo_sort(numbers))