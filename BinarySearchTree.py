class Node() :
    def __init__(self,left,right,data) :
        self.left=left
        self.right=right
        self.data=data
    def insert(self,d) :
        if d < self.data :
            if self.left==None :
                self.left=Node(None,None,d)
            else :
                self.left.insert(d)
        elif d > self.data:
            if self.right==None :
                self.right=Node(None,None,d)
            else :
                self.right.insert(d)
    def search (self,d) :
        if d < self.data :
            if self.left==None :
                return False
            else :
                return self.left.search(d)
        elif d > self.data:
            if self.right==None :
                return False
            else :
                return self.right.search(d)
        elif d==self.data :
            return True

bst= Node(None,None,3)
bst.insert(2)
bst.insert(5)
print bst.search(6)
