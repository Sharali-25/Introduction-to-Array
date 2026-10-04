def minelement(a,size):
    temp = a[0]
    for i in range(1,size):
        temp = min(temp,a[i])
    return temp
def maxelement(a,size):
    temp = a[0]
    for i in range (1,size):
        temp = max(temp,a[i])
    return temp
arr = [2,3,7,5,1,9,7,6,0,7,5,1,2,5,6,765,4,38]
size = len(arr)
print("Min element of Array = ",minelement(arr,size))
print("Maximum element of Array = ",maxelement(arr,size))