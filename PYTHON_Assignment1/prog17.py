def linear_search(arr, target):
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

my_list = [1,2,3,4,5,6]
target_value = 5
result = linear_search(my_list, target_value)

if result != -1:
    print(f"Found {target_value} at index {result}")
else:
    print(f"{target_value} not found in the list.")
