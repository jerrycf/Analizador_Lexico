class Cola:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def add(self, item):
        #self.items.insert(0,item)
        self.items.append(item)
        return

    def pop(self):
        #return self.items.pop()
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items.clear()
        return