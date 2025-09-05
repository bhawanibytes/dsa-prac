import ctypes

# insert
# remove
# __getitem__
# __delitem__


class myArray:
    def __init__(self) -> None:
        # capacity of Array
        self.size = 1
        # number of elements currently
        self.n = 0
        # c type static and referential Array
        self.A = self.makeArr(self.size)

    def makeArr(self, capacity):
        return (capacity * ctypes.py_object)()

    def __str__(self):
        arrString = ""
        for i in range(self.n):
            arrString = arrString + "'" + str(self.A[i]) + "',"
        return "[" + arrString[:-1] + "]"

    def __len__(self):
        return self.size

    def append(self, element):
        if self.size == self.n:
            self.resize(1)
        self.A[self.n] = element
        self.n = self.n + 1

    def resize(self, increment):
        newArr = self.makeArr(self.size + increment)
        self.size = self.size + increment
        for i in range(self.n):
            newArr[i] = self.A[i]
        self.A = newArr

    def pop(self):
        if self.n == 0:
            print("List is empty")
        print(self.A[self.n - 1])
        self.n = self.n - 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, ele):
        for i in range(self.n):
            if self.A[i] == ele:
                return i
        return "ValueError - not in list"


L = myArray()
L.append(5)
L.append(6)
L.append(8)
L.append(6)
L.append(8)
L.append(5)
L.append(6)
L.append(8)
L.append(6)
L.append(8)

print(L)
index = L.find(8)
print(index)
print(L)
