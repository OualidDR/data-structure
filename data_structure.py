# <-------------------arrays------------------->
# exercice:

# l=[2200, 2350, 2600, 2130, 2190]

# print(f'rep 1 : {l[1]-l[0]}')

# expense=0

# for i in range(0,3):
#     expense+=l[i]

# print(f'rep 2 : {expense}')

# print(f'rep 3 : {all(n == 2200 for n in l)}')
# print(f'rep 4 : {any(n == 2200 for n in l)}')

# l.append(1980)

# print(f'rep 5 : {l}')

# l[3] = l[3]-200

# print(f'rep 6 : {l}')
# <-------------------linked list------------------->

class Node :
    def __init__(self, data = None, next = None):

        self.data = data # the value of the node 
        self.next = next # the pointer to the next node  

class Linked_List :
    def __init__(self):
        self.head = None #initially the linked list is empty 

    def insert_at_begining(self, data) :
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_at_end(self, data) :
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
            return
        current = self.head
        while current.next :
            current = current.next
        current.next = new_node

    def insert_at(self, index, data):

        new_node = Node(data)

        if not self.head or index == 0 :
            new_node.next = self.head
            self.head=new_node
            return
        
        current = self.head
        count = 0 

        while current and count < index - 1 :
            prev = current
            count+= 1
            current = current.next

        if not current :
            print('index invalid')
            return 
        
        new_node.next=current.next
        current.next = new_node

    def instert_after(self, data, prev_node) :
        
        if prev_node is None :
            print('prev_node can\'t be None')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delet_value(self, key) :
        current = self.head
        if current and current.data == key :
            self.head = current.next
        
        while current and current.data != key :
            prev = current
            current = current.next 

        if current == None :
            print('element not found !')
            return
        prev.next = current.next

    def search (self, key) :
        current = self.head
        while current : 
            if current.data == key :
                return True
            current = current.next 
        return False
    
    def insert_from_list(self, liste):
        for i in liste : 
            self.insert_at_begining(i)
            

    def lenght(self) :
        count = 0
        current = self.head
        while current :
            count+=1
            current = current.next
        return count
    
    def del_index(self, index) :
        if not self.head : 
            print('list vide ')
            return
        
        if index<0 or index > self.lenght() :
            raise Exception('invalid index !')
        
        # delet the 1st element
        if index == 0 :
            
            self.head = self.head.next
            return
        current = self.head
        count = 0 
        while current and count < index - 1 : 
            current = current.next
            count+= 1
        if not current or not current.next : 
            print ('elem not found ')
            return
        current.next = current.next.next

    def print(self) :
        if self.head == None:
            print("linked list empty")
            return
        
        current = self.head
        while current :
            print(current.data, end=" --> ")
            current=current.next
        print("None")

# ll = Linked_List()
# data = ['a', 'b', 'c','d','e']
# ll.insert_from_list(data)
# ll.insert_at(3,'walid')
# ll.print()
# print(ll.search('a'))
# ll.delet_value('a')
# ll.print()
# print(ll.search('a'))
# print(ll.lenght())
# ll.del_index(2)
# ll.print()

# print(ll.lenght())
# <-------------------My try------------------->

# linked list has always a head remember , we have two classes linked list and node 


# class Node :
#     def __init__(self, data= None, next= None):
#             self.data = data 
#             self.next = next 

# class Linked_List :
#     def __init__(self):
#         self.head = None

#     def insert_at_big(self, data) :
#           new_node = Node(data)
#           new_node.next = self.head
#           self.head = new_node

#     def print(self) :
#         current = self.head
#         if current == None :
#               print('vide')
#               return
#         while current :
#              print(current.data, end='--->')
#              current= current.next

# ll = Linked_List()
# ll.insert_at_big(1)
# ll.insert_at_big(2)
# ll.insert_at_big(3)
# ll.insert_at_big(4)
# ll.insert_at_big(5)
# ll.print()

#   <-------------------My 2 try------------------->

# class Node :
#     def __init__(self, data = None, next = None):
#         self.data = data
#         self.next = next 

# class List :
#     def __init__(self, head = None):
#         self.head = head 


#     def insert_beggining(self, data) :
#         new_node = Node(data)#on creer une node 
#         new_node.next = self.head # on fait le mise a jour de next de la node pour pointer sur le head precedent
#         self.head = new_node  # elle devienne le nouveau head de la list 
         
#     def insert_at_end(self, data) :
#         new_node = Node(data)#on cree le node 

#         if self.head is None :#si la liste est vide donc le node est le head automatiquement 
#             self.head = new_node
#             return
#         current = self.head
#         #sinon on cree un poiteur qui parcoure la liste jusqua la fin ,
#         # avec la condition while vre c a dire quand il point pas sur node donc pass au next , une fois on point sur none donc next point suer le nouveau node ...
#         while current.next :
#             current=current.next
#         current.next = new_node
        
# <------------------another try ---------------->

# class Node :
#     def __init__(self, data = None, next = None):
#         self.data = data
#         self.next = next

# class Linked_Liste :
#     def __init__(self):
#         self.head = None

#     def insert_at_biggining(self, data) :

#         new_data = Node(data)

#         if self.head is None :
#             self.head = new_data
#             return 
        
#         new_data.next = self.head
#         self.head = new_data


#     def insert_at_end(self, data) :
#         new_node = Node(data)

#         if self.head is None :
#             self.head = new_node
#             return
        
#         current = self.head 
#         while current.next :
#             current=current.next
#         current.next=new_node

#     def insert_from_list(self,liste) :
#         for i in liste :
#             self.insert_at_end(i)

#     def insert_after(self, prev, data) :
#         new_node = Node(data)
#         if self.head is None :
#             self.head=new_node
#             return
#         current = self.head
#         while current.data != prev :
#             current = current.next 

#         new_node.next = current.next
#         current.next=new_node
    
#     def lenght(self) :
#         count = 0
#         current = self.head
#         while current :
#             count += 1
#         return count

#     def insert_with_index(self, index, data) :
#         # if index < 0 or index > self.lenght() :
#         #         print('invalid index !!')
#         #         return
#         new_node = Node(data)
#         if self.head is None or index == 0  :
#             new_node.next = self.head
#             self.head = new_node 
#             return

#         count = 0 
#         current =self.head

#         while current and count < index -1 :
                
#                 count += 1
#                 current = current.next
#         if current is None :
#                 print('invalid index !')
#                 return 

#         new_node.next = current.next
#         current.next = new_node
        
#     def print(self) :
#         if self.head is None :
#             print('list vide !')
#             return 
#         current = self.head
#         while current :
#             print(current.data, end = '->')
#             current = current.next
#         print(None)

# ll=Linked_Liste()
# ll.insert_at_biggining(4)
# ll.insert_at_biggining(3)
# ll.insert_at_biggining(2)
# ll.insert_at_biggining(1)
# ll.insert_at_end(5)
# ll.insert_from_list(['a', 'b', 'c'])
# ll.insert_after('a','walid')
# ll.insert_with_index(4,'index')
# ll.print()

# <---------------exercices------------------>

# class Node :
#     def __init__(self, data = None, next = None):
#         self.data = data
#         self.next = next

# class LinkedList :
#     def __init__(self):
#         self.head = None


#     def insert_at_biggining(self, data) :
#         new_node = Node(data)

#         if self.head is None :
#             self.head = new_node
#             return
#         new_node.next = self.head
#         self.head = new_node

#     def insert_at_end(self, data) :
#         new_node = Node(data)
#         if self.head is None :
#             self.head = new_node
#             return
        
#         current = self.head
#         while current.next :
#             current = current.next
#         current.next = new_node


#     def insert_after_value(self, value, data) :
#         new_node = Node(data)
#         if self.head is None :
#             print ('there is no value to add after ! the list is empty ')
#             return

#         current = self.head
#         while current and current.data != value :
#             current = current.next
#         if not current :
#             print('invalid value !')
#             return 
#         new_node.next = current.next
#         current.next = new_node

#     def remove_value(self, value) :
#         if self.head is None :
#             print ('the list is empty !')
#             return

#         if self.head.data == value :
#             self.head = self.head.next
#             return

#         current = self.head
#         while current and current.data != value :
#             prev = current
#             current = current.next
#         if not current :
#             print('invalid value !')
#             return
#         prev.next = current.next

#     def print(self) :
#         if self.head is None :
#             print('list vide !')
#             return 
#         current = self.head
#         while current :
#             print(current.data, end = '->')
#             current = current.next
#         print(None)

#     def print_forward(self) :
#         if self.head is None :
#             print('empty lsi !!')
#             return
#         current = self.head
#         while current :
#             print(current.data, end = '<-->')
#             current = current.next

# ll=LinkedList()
# ll.insert_at_biggining(1)
# ll.insert_after_value(1,'oualid')
# ll.insert_after_value('oualid', 'draidi')
# ll.remove_value(1)
# ll.remove_value('oualid')
# ll.print()

# <----------------doubleLinkedList--------------------->

# class Node :
#     def __init__(self, data = None, prev = None, next = None):
#         self.data = data
#         self.next = next 
#         self.prev = prev 

# class Double_linked_list :

#     def __init__(self):
#         self.head = None

#     def insert_at_biggining(self, data) :
#         new_node = Node(data)

#         if self.head is None :
#             self.head = new_node
#             return
#         new_node.next = self.head
#         self.head.prev = new_node
#         self.head = new_node
    
#     def insert_at_end(self, data) :
#         new_node = Node(data)
#         if self.head is None :
#             self.head = new_node
#             return
        
#         current = self.head
#         while current.next :
#             current = current.next
#         current.next = new_node
#         new_node.prev = current

#     def print_forward(self) :
#         if self.head is None :
#             print('empty lsi !!')
#             return
#         current = self.head
#         while current :
#             print(current.data, end = '-->')
#             current = current.next

#         print(None)

#     def print_backward(self) :
#         if self.head is None :
#             print('empty lsi !!')
#             return
#         current = self.head
#         while current :
#             current = current.next
#         while current :
#             print(current.data, end = '-->')
#             current = current.prev
#         print(None)

# <-----------------------questions------------------------->

# two pointers is method to solve problems in linkedlists 

class Node :
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList :
    def __init__(self):
        self.head = None

# find the kth node from Back
# done
    def find_kth_node_from_back(self, k) :
        if self.head is None :
            print (' the list is empty ! ')
            return
        current = self.head
        count = 0
        value = self.head
        while current :
            current = current.next
            count += 1
        if k < 0 or k > count :
            print('invalid k !')
            return

        while value and value.data != count-k :
            value = value.next
        if not value : 
            print (' there is no value in the list ! ')
            return
        print(value.data)

    def insert_at_biggining(self, data) :
        new_node = Node(data)

        if self.head is None :
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data) :
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
            return
        
        current = self.head
        while current.next :
            current = current.next
        current.next = new_node

    def insert_after_value(self, value, data) :
        new_node = Node(data)
        if self.head is None :
            print ('there is no value to add after ! the list is empty ')
            return

        current = self.head
        while current and current.data != value :
            current = current.next
        if not current :
            print('invalid value !')
            return 
        new_node.next = current.next
        current.next = new_node
# make the end node to the first node 
    def from_end_to_big(self) :
        if self.head is None :
            print (' the list is empty ')
            return
        prev = self.head
        current = self.head
        while current.next :
            prev = current 
            current = current.next 

        current.next = self.head
        self.head = current
        prev.next = None
# cheack if linked list is palindrome casac c -> a -> s -> a -> c 
# with while loop
    #   O(log(n))
    def palindrom (self) :
        if self.head is None :
            print ('the list is empty ')
            return
        current = self.head 
        L = []
        while current : 
            L.append(current.data)
            current = current.next 
        i=0
        j=len(L)-1
        while L[i] == L[j]  and j >= i :
            i += 1
            j -= 1
        if L[i] != L[j] :
            print(f'Non, it\'s not a palindrome because {L[i]} # {L[j]}')
            return
        print('yes it\'s a palandrome')
# with foor loop 
    # O(n +log(n))
    def palindrom1 (self) :
        if self.head is None :
            print ('the list is empty ')
            return
        current = self.head 
        L = []
        while current : 
            L.append(current.data)
            current = current.next 
        for i in range(int(len(L)/2)+1) :
            if L[i] != L[len(L)-i-1] :
                print(f'Non, it\'s not a palindrome because {L[i]} # {L[len(L)-i-1]}')
                return
        print('yes it\'s a palandrome')

    # recursive is in reversed linkedlist simple and double 
    




        

    def remove_value(self, value) :
        if self.head is None :
            print ('the list is empty !')
            return

        if self.head.data == value :
            self.head = self.head.next
            return

        current = self.head
        while current and current.data != value :
            prev = current
            current = current.next
        if not current :
            print('invalid value !')
            return
        prev.next = current.next

# using Turtol/rubet methode means movs node by node and the second jumps node !
# floyd CFA (Find Cycle List) called Tortoise and Hare algorithm
    def cheak_if_cycle(self):
        if self.head is None :
            print ('the list is empty !')
            return
        current1 = self.head
        current2 = self.head
        while current2 and current2.next :
            current1 = current1.next 
            current2 = current2.next.next
            if current1.data == current2.data :
                print('its a cycle list !')
                return
            
        print('this is not a cycle list')
# find middle point of a list 

    def find_middle(self) :
        if self.head is None :
            print ('the list is empty !')
            return
        current1 = self.head
        current2 = self.head
# <--we have to cheack current and current.next if it not none always if we are working withe current.next.next------->
        while current2 and current2.next :
            current1 = current1.next
            current2 = current2.next.next
             
        print(f'the middl node is {current1.data} ')
        
    
    def print(self) :
        if self.head is None :
            print('list vide !')
            return 
        current = self.head
        while current :
            print(current.data, end = ' --> ')
            current = current.next
        print(None)

    
# yes i print the reverse of a linked list successfully
# here i used a list to store values 
def print_reverse(ll : LinkedList) :
        if ll.head is None :
            print('list vide !')
            return 
        current = ll.head
        L=[]
        while current :
            L.append(current.data)
            current = current.next
        
        for i in range(len(L)-1,-1,-1) :
            print(L[i], end=' --> ')
        print(None)
# now i have to make a reversed linked list not just a print 
# here i used a liked list to create the reversed list 
def revers(l : Linked_List) :
    if l.head is None :
        print('list vide !')
        return
    ll = Linked_List()
    current = l.head
    while current :
        ll.insert_at_begining(current.data)
        current = current.next
    ll.print()

    


# cheack if two linked lists have intersection point
# i cheaked out with gpt 
def lenght(head) :
        count = 0
        current = head
        while current :
            count+=1
            current = current.next
        return count
# we can't mak operations between methods !!!!!!!!!!


# here is a probleme i cheack out the data not nodes wich is not the objectf !!!!!!!!!!!!!
def cheack(l1 : LinkedList, l2 : LinkedList) :
    if not l1.head or not l2.head :
        print('one of the lists is empty !')
        return  
    # cheak wich of lists is longer 
    current1 = l1.head
    current2 = l2.head
    len1 = lenght(l1.head)
    len2 = lenght(l2.head)
    if  len1 > len2 :
        for i in range (len1-len2) :
            current1 = current1.next
    else : 
        for i in range(len2-len1) :
            current2 = current2.next
    while current1 and current2 :
        if current2 == current1 :
            print (f'yes there is an intersection at {current1.data}')
            return
        current1 = current1.next
        current2 = current2.next
    print('no there is no intersection point !')
    
# I did it with my self successfully alhamdolilllaaaaah 
 
def remov_duplic(l : Linked_List) :
    if not l.head  :
        print(' the list is empty !')
        return 
    s = set()
    t = Linked_List()
    current = l.head
    while current :
        s.add(current.data)
        current = current.next
    for i in s :
        t.insert_at_end(i)
    t.print()

def make_intersection_point(l1 : Linked_List, l2 : Linked_List) :
    if not l1.head or not l2.head : 
        print('empty linked listes!')
        return

    current1 = l1.head
    current2 = l2.head
        
    while current2.next :
        current2 = current2.next
    n = lenght(l1.head)
    if n > 3 :
        for i in range(lenght(l1.head)-3) :
            current1 = current1.next
    current2.next = current1
    







# ll=LinkedList()



# ll.insert_at_biggining('c')
# ll.insert_at_biggining('a')
# ll.insert_at_biggining('s')
# ll.insert_at_biggining('q')
# ll.insert_at_biggining('c')

# ll.insert_at_biggining(1)
# ll.print()
# ll.from_end_to_big()

# ll.print()
# ll.palindrom()
# ll.palindrom1()

# ll1 = LinkedList()

# ll1.insert_at_biggining(1)
# ll1.print()

# make_intersection_point(ll, ll1)
# ll1.print()
# cheack(ll, ll1)
# ll2 = LinkedList()
# ll2.insert_at_biggining(6)
# ll2.insert_at_biggining(5)
# ll2.insert_at_biggining(4)
# ll2.insert_at_biggining(3)
# ll2.print()
# cheack(ll1,ll2)

# revers(ll)
# print_reverse(ll)


# recursive factoriel 
def fact(n : int) :
    if  n <= 1 :
        return 1
    else:
        return n*fact(n-1)

# <------------------------hash_maps_implementation---------------------->

class HashTable :
    def __init__(self):
        self.max =5
        self.arr = [None for item in range(self.max)]

    def get_hash(self, key) :
        h = 0 
        for char in key :
            h += ord(char)
        return h % self.max
        

    def add(self, key, val ) :
            h = self.get_hash(key)
            self.arr[h] = val 
    
    def get(self, key) :
        h = self.get_hash(key)
        return self.arr[h]



         
hash = HashTable()
print(hash.get_hash('walid'))

# les collisions  
# Une collision arrive quand deux clés différentes produisent le même index après hachage.