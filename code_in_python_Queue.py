#code_in_python
#queue_implemention


class Queue :
    def __init__(self) :
        self.list=[]

    def enqueue(self,data) :
        self.list.insert(0,data)
        print ("After inserting "+(str)(data))
        temp=self.list
        #temp.reverse()
        print(temp)

    def dequeue(self) :
        self.list.pop()
        print ("After remove")
        temp=self.list
        #temp.reverse()
        print(temp)

    def isEmpty(self) :
        return self.list==[]

    def size(self) :
        return len(self.list)


qobj=Queue()
qobj.enqueue(5)
qobj.enqueue(10)
qobj.enqueue(7)
qobj.dequeue()
qobj.enqueue(7)
