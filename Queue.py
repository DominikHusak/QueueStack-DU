class Node:
    def __init__(self, data):
        self.data = data #Hodnota ulozena ve fronte
        self.next = None #Nasledujici prvek
        self.prev = None #Predchozi prvek
    #Inicializace obousmerneho uzlu fronty

class Queue:
    def __init__(self):
        self.head = None #Vrchol fronty
        self.tail = None #Spodek fronty
        self.size = 0 #velikost fronty
    #Inicializace tridy Queue(Fronta)


    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    #Prida prvek na konec fronty


    def pop(self):
        if self.head is None:
            raise Exception("Fronta je prazdna.")
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        self.size -= 1
        return data
    #Odstrani prvni prvek fronty
    #Raise vyhodi vyjimkuv pripade ze fronta je prazdna 


    def count(self):
        return self.size
    #Vrati pozet prvku v zasobniku 


    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
    #Vyprazdni frontu


    def popAll(self):
        elements = []
        while self.head is not None:
            elements.append(self.pop())
        return elements
    #Ziska a vrati vsechny prvky fronty a vyprazdni ji



queue = Queue()
queue.add(1)
queue.add(2)
queue.add(3)
popped_item = queue.pop()
print(f"Vyhozeny prvek: {popped_item}")
print(f"Pocet prvku ve fronte: {queue.count()}")  
queue.clear()  
print(f"Pocet prvku ve fronte: {queue.count()}")  
queue.add(4)
queue.add(5)
queue.add(6)
print(queue.popAll()) 