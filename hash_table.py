
class hashfunc :
    def __init__(self) :
        self.size=11
        self.slots=[None for i in range(11)]
        self.data=[None for i in range(11)]
    def put(self,key,data) :
        val=key%self.size
        self.slots[val]=key
        self.data[val]=data
    def get(self,key):
        if key in self.slots :
            return self.data[self.slots.index(key)]
    def __getitem__(self,key) :
        return self.get(key)
    def __setitem__(self,key,data) :
        self.put(key,data)


H=hashfunc()
H[100]=1
print H.slots
print H.data
print H[10]
