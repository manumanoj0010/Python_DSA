class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class Linkedlist():
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        end = self.head
        while(end.next):
            end = end.next
        
        end.next = Node(data, None)
        
    def get_length(self):
        count = 0
        nxt = self.head
        while nxt:
            count+=1
            nxt = nxt.next
        
        return count
        
    def insert_values(self, data_list):  #new linkedlist with the list of values
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            print("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        nxt = self.head
        while nxt:
            if count == index-1:
                nxt.next = nxt.next.next
                break
            nxt = nxt.next
            count+=1
    
    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            print("Index out of range. Please check your index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        nxt = self.head
        while(nxt):
            if count == index-1:
                node = Node(data, nxt.next)
                nxt.next = node
                break
            
            nxt = nxt.next
            count+=1            
        
    def print_linkedlist(self):
        if self.head is None:
            print("Linked List is empty")
            return
    
        nxt = self.head
        linked_list = ''
        while nxt:
            linked_list += str(nxt.data) + '-->'
            nxt = nxt.next
        
        print(linked_list)
        
        
    
a = Linkedlist()
a.insert_at_beginning(5)
a.insert_at_beginning(25)
a.insert_at_end(100)
a.insert_values(["banana","apples","abcd","adaewfwf"])
a.remove_at(3)
a.insert_at(1,"manoj")
print(a.get_length())
a.print_linkedlist()