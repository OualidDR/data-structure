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

# class Node :
#     def __init__(self, data = None, next = None):

#         self.data = data # the value of the node 
#         self.next = next # the pointer to the next node  

# class Linked_List :
#     def __init__(self):
#         self.head = None #initially the linked list is empty 

#     def insert_at_begining(self, data) :
#         new_node = Node(data)
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

#     def insert_at(self, index, data):

#         new_node = Node(data)

#         if not self.head or index == 0 :
#             new_node.next = self.head
#             self.head=new_node
#             return
        
#         current = self.head
#         count = 0 

#         while current and count < index - 1 :
#             prev = current
#             count+= 1
#             current = current.next

#         if not current :
#             print('index invalid')
#             return 
        
#         new_node.next=current.next
#         current.next = new_node
        
        
             
        
    
#     def instert_after(self, data, prev_node) :
        
#         if prev_node is None :
#             print('prev_node can\'t be None')
#             return
#         new_node = Node(data)
#         new_node.next = prev_node.next
#         prev_node.next = new_node

#     def delet_value(self, key) :
#         current = self.head
#         if current and current.data == key :
#             self.head = current.next
        
#         while current and current.data != key :
#             prev = current
#             current = current.next 

#         if current == None :
#             print('element not found !')
#             return
#         prev.next = current.next

#     def search (self, key) :
#         current = self.head
#         while current : 
#             if current.data == key :
#                 return True
#             current = current.next 
#         return False
    
#     def insert_from_list(self, liste):
#         for i in liste : 
#             self.insert_at_begining(i)
            

#     def lenght(self) :
#         count = 0
#         current = self.head
#         while current :
#             count+=1
#             current = current.next
#         return count
    
#     def del_index(self, index) :
#         if not self.head : 
#             print('list vide ')
#             return
        
#         if index<0 or index > self.lenght() :
#             raise Exception('invalid index !')
        
#         # supprimer le 1er elem
#         if index == 0 :
            
#             self.head = self.head.next
#             return
#         current = self.head
#         count = 0 
#         while current and count < index - 1 : 
#             current = current.next
#             count+= 1
#         if not current or not current.next : 
#             print ('elem not found ')
#             return
#         current.next = current.next.next

#     def print(self) :
#         if self.head == None:
#             print("linked list empty")
#             return
        
#         current = self.head
#         while current :
#             print(current.data, end=" --> ")
#             current=current.next
#         print("None")

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

#                  <-------------------My 2 try------------------->


class Node :
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next 

class List :
    def __init__(self, head = None):
        self.head = head 


    def insert_beggining(self, data) :
        new_node = Node(data)#on creer une node 
        new_node.next = self.head # on fait le mise a jour de next de la node pour pointer sur le head precedent
        self.head = new_node  # elle devienne le nouveau head de la list 
         
    def insert_at_end(self, data) :
        new_node = Node(data)#on cree le node 

        if self.head is None :#si la liste est vide donc le node est le head automatiquement 
            self.head = new_node
            return
        current = self.head
        #sinon on cree un poiteur qui parcoure la liste jusqua la fin ,
        # avec la condition while vre c a dire quand il point pas sur node donc pass au next , une fois on point sur none donc next point suer le nouveau node ...
        while current.next :
            current=current.next
        current.next = new_node
        

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
    


    def print(self) :
        if self.head is None :
            print('list vide !')
            return 
        current = self.head
        while current :
            print(current.data, end = '->')
            current = current.next
        print(None)

    

# yes i print the reverse of a linked list successfully
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
            print(L[i], end='-->')
        print(None)

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
        if current2.data == current1.data :
            print (f'yes ther is an intersection at {current1.data}')
            return
        current1 = current1.next
        current2 = current2.next
    print('no there is no intersection point !')



ll=LinkedList()


ll.insert_at_biggining(5)
ll.insert_at_biggining(6)
ll.insert_at_biggining(4)
ll.insert_at_biggining(3)
ll.insert_at_biggining(2)
ll.insert_at_biggining(1)
ll.print()

print_reverse(ll)


ll1 = LinkedList()


ll1.insert_at_biggining(5)
ll1.insert_at_biggining(6)
ll1.insert_at_biggining(9)
ll1.print()
print_reverse(ll1)
cheack(ll,ll1)