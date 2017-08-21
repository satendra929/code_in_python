#code_in_python
#binary_search_tree

class Node :
    def __init__(self,val) :
        self.val=val
        self.leftChild=None
        self.rightChild=None

    def insert(self,data) :
        if self.val==data :
            return False
        elif self.val > data :
            if self.leftChild :
                return self.leftChild.insert(data)
            else :
                self.leftChild=Node(data)
                return True
        else :
            if self.rightChild :
                return self.rightChild.insert(data)
            else :
                self.rightChild=Node(data)
                return True

    def search (self,data) :
        if self.val==data :
            return True
        elif self.val>data :
            if self.leftChild :
                return self.leftChild.search(data)
            else :
                return False
        else :
            if self.rightChild :
                return self.rightChild.search(data)
            else :
                return False

obj=Node(5)
print(obj.insert(6))
print (obj.insert(10))
print (obj.insert(11))
print (obj.search(1))
