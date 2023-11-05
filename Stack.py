class Node:
    def __init__(self, value):
        self.value = value #Hodnota ulozena v zasobniku
        self.next = None #Nasledujici prvek
    #Inicializace jednosmerneho uzlu zasobniku


class Stack:
    def __init__(self):
        self.top = None #Vrchol zasobniku
        self.size = 0 #Velikost zasobniku
    #Inicializace tridy Stack(Zasobnik)


    def add(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    #Vlozi novy prvek na vrchol zasobniku


    def pop(self):
        if self.top is None:
            raise Exception("Zasobnik je prazdny")
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value
    #Odstrani prvek z vhrcholu zasobniku
    #Raise vyhodi vyjimku v pripade ze zasobnik je prazdny


    def count(self):
        return self.size
    #Vrati pozet prvku v zasobniku 


    def clear(self):
        self.top = None
        self.size = 0
    #Vyprazdni cely zasobnik


    def popAll(self):
        elements = []
        while self.top:
            elements.append(self.pop())
        return elements
    #Ziska a vrati vsechny prvky zasobniku a vyprazdni ho
    


stack = Stack()
stack.add(1)
stack.add(2)
stack.add(3)
print(f"Prvky v zasobniku: {stack.count()}")
popped_item = stack.pop()
print(f"Vyhozeny prvek: {popped_item}")
print(f"Prvky v zasobniku: {stack.count()}")
stack.clear()
print(f"Vyprazdneni zasobniku: {stack.count()}")
stack.add(4)
stack.add(5)
stack.add(6)
all_elements = stack.popAll()
print(f"Vsechny prvky: {all_elements}")
print(f"Pocet prvku v zasobniku: {stack.count()}")
