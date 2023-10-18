
def find_largest_number(arr):
    if len(arr) == 0:
        return None  

    largest = arr[0] 

    for number in arr:
        if number > largest:
            largest = number

    return largest
my_list = [10,67,4,89,56,90,46]
largest_number = find_largest_number(my_list)
   print("The largest number in the list is:", largest_number)
