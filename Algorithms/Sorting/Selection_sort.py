# <!-------By manumanoj----------->

#Ascending order

Data1 = [75,3,73,7,6,23,89,8]

for i in range(len(Data1)-1):
    min_num = min(Data1[i:])
    min_ind = Data1.index(min_num,i)
    if Data1[i] != Data1[min_ind]:
        Data1[i], Data1[min_ind] = Data1[min_ind], Data1[i]
print(Data1)

#Descending order

Data2 = [75,3,73,7,6,23,89,8]

for i in range(len(Data2)-1):
    max_num = max(Data2[i:])
    max_ind = Data2.index(max_num,i)
    if Data2[i] != Data2[max_ind]:
        Data2[i], Data2[max_ind] = Data2[max_ind], Data2[i]
    
print(Data2)