# <!-------By manumanoj----------->

#Ascending order

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
for i in range(n):
    for j in range(n-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
print(a)

#Descending order

Data = [75,3,73,7,6,23,89,8]
for i in range(len(Data)):
    for j in range(len(Data)-1):
        if(Data[j]<Data[j+1]):
            Data[j],Data[j+1]=Data[j+1],Data[j]
print(Data)