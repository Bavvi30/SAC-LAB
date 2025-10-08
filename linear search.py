def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 25, 30, 45, 50]
target = 30
result = linear_search(arr, target)
if result != -1:
    print(f"element {target} found at index {result}")
else:
    print(f" element {target} not found")
