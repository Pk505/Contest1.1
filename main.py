class deque:
    def __init__(self, memory):
        self.values = [-1] * memory
        self.size = 0
        self.start = 0
        self.end = 0
        self.memory = memory

    def print(self):
        if self.size == 0:
            print("empty")
        else:
            index = self.start
            for i in range(self.size):
                if index == self.memory:
                    index = 0
                print(self.values[index], end=' ')
                index += 1
            print()

    def pushb(self, value):
        if self.size == 0:
            self.values[self.end] = value
            self.size += 1
        else:
            if self.size < self.memory:
                if self.end != self.memory - 1:
                    self.end += 1
                else:
                    self.end = 0
                self.values[self.end] = value
                self.size += 1
            else:
                print("overflow")

    def pushf(self, value):
        if self.size == 0:
            self.values[self.start] = value
            self.size += 1
        else:
            if self.size < self.memory:
                if self.start != 0:
                    self.start -= 1
                else:
                    self.start = self.memory - 1
                self.values[self.start] = value
                self.size += 1
            else:
                print("overflow")

    def popb(self):
        if self.size == 0:
            print("underflow")
        else:
            print(self.values[self.end])
            self.values[self.end] = -1
            self.size -= 1
            if self.end != 0:
                self.end -= 1
            else:
                self.end = self.memory - 1

    def popf(self):
        if self.size == 0:
            print("underflow")
        else:
            print(self.values[self.start])
            self.values[self.start] = -1
            self.size -= 1
            if self.start != self.memory - 1:
                self.start += 1
            else:
                self.start = 0




entered_deque = deque(5)
entered_deque.pushb(1)
entered_deque.pushb(2)
entered_deque.pushb(3)
entered_deque.pushf(5)
entered_deque.print()
entered_deque.popb()
entered_deque.print()
entered_deque.popf()
entered_deque.print()
