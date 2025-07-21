class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0
   

    def push(self, item):
        if len(self.items)>= self.limit:
            print("Stack is full")
        else: 
            self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        try: 
            index_from_top = self.items[::-1].index(target)
            return index_from_top
        except ValueError:
            return -1
            
        
