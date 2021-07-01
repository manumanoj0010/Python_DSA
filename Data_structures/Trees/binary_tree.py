class Binary_tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self,data):
        if data == self.data:
            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Binary_tree(data)
            
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Binary_tree(data)
                
    def search(self,val):
        if val==self.data:
            return True
        
        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
                
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
    def in_order_traversal(self):
        l=[]
        if self.left:
            l+=self.left.in_order_traversal()
        
        l.append(self.data)
        
        if self.right:
            l+=self.right.in_order_traversal()
        
        return l
    
    def pre_order_traversal(self):
        l=[]
        
        l.append(self.data)
        
        if self.left:
            l+=self.left.pre_order_traversal()
        
        if self.right:
            l+=self.right.pre_order_traversal()
        
        return l

    def post_order_traversal(self):
        l=[]
        
        if self.left:
            l+=self.left.post_order_traversal()
        
        if self.right:
            l+=self.right.post_order_traversal()
            
        l.append(self.data)
        
        return l
    
    
def build_tree(elements):
    root = Binary_tree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
            
if __name__ =='__main__':
    numbers = build_tree([17,4,1,20,9,23,18,24])
    print("In order traversal gives this sorted list:", numbers.in_order_traversal())
    print("Pre order traversal gives this sorted list:", numbers.pre_order_traversal())
    print("Post order traversal gives this sorted list:", numbers.post_order_traversal())
    
    