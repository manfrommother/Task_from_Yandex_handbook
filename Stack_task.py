class Stack():

    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def is_empty(self):
        if len(self.list) > 0:
            return False
        else:
            return True

    def pop(self):
        total = self.list[0]
        del self.list[0]
        return total


stack = Stack()
for item in ("Hello,", "world!"):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop())
#test comment