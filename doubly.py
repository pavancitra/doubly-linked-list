class node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def add_begin(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.nref=self.head
            self.head.pref=newnode
            self.head=newnode
    def add_end(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            return
        n=self.head
        while n.nref is not None:
            n=n.nref
        newnode.pref=n
        n.nref=newnode
    def add_before(self,data,x):
        newnode = node(data)
        if self.head is None:
            print("empty linked list")
            return
        if self.head.data==x:

            self.head.pref=newnode
            newnode.nref=self.head
            self.head=newnode
            return
        n=self.head
        while n.nref is not None:
            if n.nref.data==x:
                break
            else:
                n=n.nref
        if n.nref is None:
            print("node not present")
        else:

            newnode.pref=n
            newnode.nref=n.nref
            n.nref = newnode
            n.nref.pref=newnode
    def add_after(self,data,x):
        if self.head is None:
            print("empty linked list")
            return
        n=self.head
        while n is not None:
            if n.data==x:
                break
            else:
                n=n.nref
        if n is None:
            print("node not present in linked list")
        else:
            newnode=node(data)
            newnode.pref=n
            newnode.nref=n.nref
            if n.nref is not None:
                n.nref.pref=newnode
            n.nref=newnode


    def traversal(self):
        if self.head is None:
            print("empty linked list")
            return
        n=self.head
        while n is not None:
            print(n.data,"-->",end=" ")
            n=n.nref
    def delete_b(self):
        if self.head is None:
            print("empty linked list")
            return
        else:
            if self.head.nref is not None:
                self.head=self.head.nref
                self.head.pref=None
            else:
                self.head=None
    def delete_e(self):
        if self.head is None:
            print("empty linked list")
            return
        if self.head.nref is None:
            self.head=None
            return
        n=self.head
        while n.nref is not None:
            n=n.nref
        n.pref.nref=None
    def delete_by(self,x):
        if self.head is None:
            print("empty linked list")
            return
        if self.head.nref is None:
            if self.head.data==x:
                self.head=None
                print("empty linked list")
                return
            else:
                print("node not present")
                return
        n=self.head
        while n is not None:
            if n.data==x:
                break
            else:
                n=n.nref
        if n is None:
            print("node not present")
        else:
            n.pref.nref=n.nref
            if n.nref is not None:
                n.nref.pref=n.pref

n1=linkedlist()
n1.add_begin(20)
n1.add_begin(10)
n1.add_end(30)
n1.add_end(40)
n1.add_before(50,20)
n1.add_after(90,50)

n1.delete_b()
n1.delete_e()
n1.delete_by(20)
n1.traversal()
