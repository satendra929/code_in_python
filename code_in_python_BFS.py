#code_in_python
#BFS_implementation

class Queue :
    def __init__(self) :
        self.list=[]

    def enqueue(self,data) :
        self.list.insert(0,data)

    def dequeue(self) :
        return self.list.pop()

    def isEmpty(self) :
        return self.list==[]
    def contain(self,data) :
        if data in self.list :
            return True
        else :
            return False
    def size(self) :
        return len(self.list)
    def givelist(self) :
        return self.list


#implementiing a graph first using a dictionary

graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}


qobj=Queue()
qobj.enqueue('A')
visited=[]


while (qobj.isEmpty()==False) :
    node=qobj.dequeue()
    if node not in visited :
        visited.append(node)
        neighbours=graph[node]
        for n in neighbours :
            if qobj.contain(n) == False :
                qobj.enqueue(n)
    print (qobj.givelist())
    print ("Visited")
    print (visited)








