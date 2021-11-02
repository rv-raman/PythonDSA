class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_end(self,n):
        node = Node(n,None)
        if self.head is None:
            self.head = node
        else:
            itr = self.head
            while (itr.next)!=None:
                itr=itr.next
            itr.next = node

    def insert_at_begininning(self,n):
        node = Node(n,None)
        node.next = self.head
        self.head=node

    def insert_values(self,lst):
        for i in lst:
            self.insert_at_end(i)

    def len_of_ll(self):
        if self.head==None:
            return 0
        else:
            itr = self.head
            cnt=0
            while itr!=None:
                cnt+=1
                itr=itr.next
            return cnt

    def remove_at(self,n):
        if n<0 or n>=self.len_of_ll():
            raise Exception("not valid index")
        if n==0:
            self.head = self.head.next
        else:
            cnt=1
            itr = self.head
            while(cnt<=n-1):
                cnt+=1
                itr=itr.next
            itr.next = itr.next.next


    def print(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            itr = self.head
            while(itr!=None):
                print(itr.data,end=" ")
                itr=itr.next
        print()

    def remove_by_value(self,n):
        prev=None
        itr =self.head
        if itr.data==n:
            self.head = itr.next
            return
        while itr!=None and itr.data!=n:
            prev=itr
            itr=itr.next
        if itr==None:
            print("element does not exist")
            return
        prev.next = itr.next

    def insert_after_value(self,data_after, data_to_insert):
        itr = self.head
        while itr.data!=(data_after):
            itr = itr.next
        node = Node(data_to_insert,None)
        node.next = itr.next
        itr.next = node


    def insert_at(self,pos,n):
        if pos<0 or pos>self.len_of_ll():
            raise Exception("not valid index")
        if pos==0:
            node = Node(n,self.head)
            self.head = node
        else:
            cnt=1
            itr = self.head
            print("itr has ",itr.data)
            while cnt<=pos-1:
                itr=itr.next
                cnt+=1
            temp = itr.next
            node = Node(n,None)
            node.next = temp
            itr.next = node





if __name__=="__main__":
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
