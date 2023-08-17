class Node:
    """ An object for storing a single node of a linked list models two attributes data and link to the next node in the list """
    data=None
    next_node=None
    def __init__(self,data):
        self.data=data

    def __repr__(self):
        return "<Node data: %s>" %self.data
class LinkedList:
    """ Singly linked list """
    def __init__(self):
        self.head=None
    def is_empty(self):
        return self.head==None #if its true then the list is empty
    def size(self):
        """ Returns no.of nodes in the list, takes O(n) time """
        current=self.head
        count=0
        while current: #same as while(current != None)
            count=count+1
            current=current.next_node #in tail node when we check next_node it returns None
        return count
    def add(self,data):
        """ Adds a new node having data at head of the list, takes constant time """
        new_node=Node(data)
        new_node.next_node=self.head
        self.head=new_node
    def search(self,key):
        """ Search for the first node containing data that matche the key and returns node or none if not found, Takes O(n) time """
        current=self.head
        while current:
            if current.data==key:
                return current
            else:
                current=current.next_node
        return None
    def insert(self,data,index):
        """ Inserts a new node with data at the given index, takes constant time but finding the node at insertion point takes O(n) time therefore takes O(n) time """
        if index==0:
            self.add(data)
        if index>0:
            new=Node(data)
            position=index
            current=self.head
            
            while position>1:
                current=current.next_node
                position-=1
            prev_node=current
            next_ndode=current.next_node
            prev_node.next_node=new
            new.next_node=next_ndode
    def removei(self,index):
        current=self.head
        if index==0:
            self.head=current.next_node
        if index>0:
            position=index
            while position>1:
                current=current.next_node
                position-=1
            prev_node=current
            current=current.next_node
            position-=1
            prev_node.next_node=current.next_node
    def remove(self,key):
        """ Removes the node with data that matches the key, returns the node or none if key dosen't exist take O(n) time"""
        current=self.head
        previous=None
        found=False
        while current and not found:
            if current.data==key and current == self.head :
                found=True
                self.head=current.next_node
            elif current.data == key:
                found= True
                previous.next_node =current.next_node
            else:
                previous = current
                current=current.next_node
    def node_at_index(self,index):
        if index==0:
            return self.head
        else:
            current=self.head
            position=0
            while position<index:
                current=current.next_node
                position+=1
        return current
                
    
    def __repr__(self):
        """ Return a string representation of the list, takes O(n) time """ 
        nodes=[]
        current=self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" %current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" %current.data)
            else:
                nodes.append("[%s]" %current.data)
            current=current.next_node
        return"->".join(nodes)