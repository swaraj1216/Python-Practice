#Binary Search
import math
list = [10,20,34,678,123,89,30,40,79,23,89,50]
list.sort()
print(list)
target = int(input("Enter The Target Element You Want To Find in The List: "))
left = 0
right= len(list) - 1
while (left<=right):
    mid = (left + right)//2
    if list(mid == target):
        print(target,"found at index",mid)
        break
    elif list(mid<target):
        left = mid + 1
    else:
        right = mid - 1
else:
    print(target, "not found in the given list.")