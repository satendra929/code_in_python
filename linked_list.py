class node :
    def __init__(self):
        self.data=None
        self.next=None


class linked_list :
    def __init__(self) :
        self.cur_node=None
    def add_node(self,data) :
        new_node=node()
        new_node.data=data
        new_node.next=self.cur_node
        self.cur_node=new_node

    def list_print(self) :
        node=self.cur_node
        while node :
            print node.data
            node=node.next
    def search(self,data) :
        node=self.cur_node
        while node :
            if node.data==data :
                print "Found"
            node=node.next
    def remove(self,data) :
        node=self.cur_node
        if node.data==data :
            self.cur_node=node.next
            return True
        while node :
            node2=node.next
            if node2.data==data :
                node.next=node2.next
                return True
            node=node.next
        return False

ll = linked_list()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.list_print()
ll.search(2)
ll.remove(1)
ll.list_print()
