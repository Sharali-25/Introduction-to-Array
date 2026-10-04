# 1) Create a function to calculate the mean of a list:
# a) Add all elements using a loop.
# b) Mean = total sum / number of elements.
# c) Return the mean as a float.
# 2) Create a function to calculate the median of a list:
# a) Sort the list first.
# b) If the size is odd, return the middle element.
# c) If the size is even, return the average of the two middle elements.
# 3) Create a sample list and find its size using `len()`.
# 4) Call both functions and print the mean and median.
def arraymean(arr,arr_size):
    total_sum = 0
    for i in range(0,arr_size):
        total_sum += arr[i]
    return total_sum//arr_size 
def arraymedian(arr,arr_size):
    arr.sort()
    if arr_size%2 !=0:
        return float(arr[int(arr_size/2)])
    return float((arr[int((arr_size-1)/2)]+ arr[int(arr_size/2)])/2.0)

arr = [1,5,3,7,6,7,8,0,9,2,4]
arr_size = len(arr)
print("Mean = ",arraymean(arr,arr_size))
print("Median = ", arraymedian(arr,arr_size))