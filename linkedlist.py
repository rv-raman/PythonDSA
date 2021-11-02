class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Linkedlist():
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

    def insert(self,lst):
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


    def printl(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            itr = self.head
            while(itr!=None):
                print(itr.data,end=" ")
                itr=itr.next
        print()

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
    ll = Linkedlist()
    ll.insert([5,2,1,3,4,12323,234521,1,1])
    length= ll.len_of_ll()
    print(length)
    ll.printl()
    ll.insert_at(9,444)
    ll.printl()