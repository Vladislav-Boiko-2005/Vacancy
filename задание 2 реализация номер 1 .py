'''вариант реализации номер 1
Минусом этой реализации является возможная просадка по времени,
если очередь превысит свой изначальный предел, и нужно будет её перезаписать.
Плюсом данной реализации является оптимальное использование памяти программой'''
class Queue:
    def __init__(self, initial_size=10):
        if initial_size<=0:initial_size=1
        self.size = initial_size
        self.buffer = [None] * self.size
        self.head = 0
        self.tail = 0
        self.count = 0

    def push(self, item):
        if self.count == self.size:
            self.resize(self.size * 2)

        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def get(self):
        if self.count == 0:
            print("пока пусто")
            return 0
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return item

    def resize(self, new_size):
        new_buffer = [None] * new_size
        for i in range(self.count):
            new_buffer[i] = self.buffer[(self.head + i) % self.size]
        self.buffer = new_buffer
        self.size = new_size
        self.head = 0
        self.tail = self.count

    def __len__(self):
        return self.count
