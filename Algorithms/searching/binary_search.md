# Binary Search 

>Time Complexity O(log n)

### Iterative Binary Search

```python
def Binary_Iterative(data, target):
    low = 0
    high = len(data)-1
    while low <= high:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target <= data[mid]:
            high = mid -1
        else:
            low = mid + 1
    return False
```

### Recursive Binary Search
```python
def Binary_Recursive(data, target, high, low):
    if low > high:
        return False
    else:
        mid = (high + low)//2
        if target == data[mid]:
            return True
        elif target <= data[mid]:
            return Binary_Recursive(data, target, mid-1, low)
        else:
            return Binary_Recursive(data, target, high, mid+1)
```

```python
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
          21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
          31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
          41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
          51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
          61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
          71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
          81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
          91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

target = int(input("Enter your target number: "))

print(Binary_Iterative(data, target))
print(Binary_Recursive(data, target, len(data)-1, 0))
```