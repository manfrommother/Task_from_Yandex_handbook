class RedButton():

    def __init__(self):
        self.counter = 0

    def click(self):
        print('Тревога!')
        self.counter += 1

    def count(self):
        return self.counter



first_b = RedButton()

for _ in range(5):
    first_b.click()

print(first_b.count())
