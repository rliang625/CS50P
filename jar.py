class Jar:
    def __init__(self, capacity = 12):
        if type(capacity) != int or capacity < 1:
            raise ValueError ("Wrong Capacity")
        else:
            self._capacity = capacity
            self._size = 0

    def __str__(self):
        cookies = ""
        for i in range (self._size):
            cookies+=("🍪")
        return cookies

    def deposit(self, n):
        if self._size + n > self.capacity:
            raise ValueError ("Over Capacity")
        else:
            self._size += n

    def withdraw(self, n):
        if self._size - n >= 0:
           self._size -= n
        else:
            raise ValueError ("Not Enough Cookies")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

one_Jar = Jar()
one_Jar.deposit(4)
one_Jar.withdraw(2)
print(one_Jar.size)