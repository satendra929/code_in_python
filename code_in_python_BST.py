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
        elif self.val :
            self.val.insert(data)
        else :
            if self.val > data :
                self.leftChild=Node(data)
            else :
                self.RightChild=Node(data)

obj=Node(5)
obj.insert(6)
