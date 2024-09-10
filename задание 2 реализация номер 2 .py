"""Задание номер 2 реализация номер 2, через списки
Улучшение времени выполнения программы относительно 1 реализации (но не значительное, т.к. метод pop оптимизирован),
Но ухудшение по использованию памяти, её большие затраты относительно 1 способа
"""
class Queue:
    def __init__(self):
        self.items = []

    def push_back(self, item):
        self.items.append(item)

    def get(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error")
            return -1
    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

