```python

#s = source
#h = helper
#d = destination

def tower_of_hanoi(n,a,b,c):
    if n==1:
        print("Move 1st from", a, "to" , c)
        return
    tower_of_hanoi(n-1, a, c, b)
    print("move", n, "th disk from",a, "to", c)
    tower_of_hanoi(n-1, b, a ,c)
    
tower_of_hanoi(4,'s','h','d') 

```