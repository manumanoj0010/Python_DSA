# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
value = [60,100,120]
weight = [10,20,30]
w=50
n=len(value)
#recursive approach
def knapsack(weight,value,w,n):
    if(n==0 or w==0):
        return 0
    if (weight[n-1]<=w):
        return max(value[n-1]+knapsack(weight,value,w-weight[n-1],n-1),knapsack(weight,value,w,n-1))
    elif(weight[n-1]>w):
        return knapsack(weight,value,w,n-1)
    
print(knapsack(weight,value,w,n))
        
#recursive with memoization

t = [[-1 for i in range(w+1)] for j in range(n+1)]

def memo_knapsack(weight,v,w,n):
    if(n==0 or w==0):
        return 0
    if t[w][n]!=-1:
        return t[n][w]
    
    if weight[n-1]<w:
        t[n][w]=max(v[n-1]+memo_knapsack(weight,v,w-weight[n-1],n-1), memo_knapsack(weight,v,w,n-1))
        return t[n][w]
    
    elif weight[n-1]>w:
        t[n][w]=knapsack(weight,v,w,n-1)
        return t[n][w]
        
print(memo_knapsack(weight,value,w,n))

#iterative 


