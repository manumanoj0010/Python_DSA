> Note Binary search works only on sorted integers.

Example:

data =  [1,3,5,6,7,8,9,12,14,23,32,56,75]<br>
target = 10
output = 9
9 is the closest number to the 10

target = 100
output = 75
75 is the closest number to the 100



```python

def closest_number(data, target):
    min_value = float("inf")
    low = 0
    high = len(data) - 1
    close_num = None
    
    #if list is empty
    if len(data) == 0:
        return None
    
    #if list has only one element
    if len(data) == 1:
        return data[0]
    
    while low <= high:
        mid = (high + low)//2
        
        #boundry limits
        if mid+1<len(data):
            min_value_right = abs(data[mid+1]-target)
        
        if mid>0:
            min_value_left = abs(data[mid-1]-target)
        
        #checking the smallest value from right and left neighbours
        
        if min_value_left < min_value:
            min_value = min_value_left
            close_num = data[mid-1]
        
        if min_value_right < min_value:
            min_value = min_value_right
            close_num = data[mid+1]
        
        #moving the mid value for next loop
        if data[mid]<target:
            low = mid+1
        
        elif data[mid]>target:
            high = mid -1
        
        #if target is the mid value
        
        else:
            return data[mid]
    return close_num
            
data = [1,3,5,6,7,8,9,12,14,23,32,56,75]
target = int(input("Enter your target number: ")) 
        
num = closest_number(data, target)
print(num)
```
