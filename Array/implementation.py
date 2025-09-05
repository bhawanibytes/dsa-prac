import ctypes


# remove
# extras features:
# sort/min/max/sum
# extend
# negative indexing
# slicing
# merge
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
            return Exception("List is empty")
        print(self.A[self.n - 1])
        self.n = self.n - 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, ele):
        for i in range(self.n):
            if self.A[i] == ele:
                return i
        raise ValueError(f"ValueError - {ele} not in list")

    def __getitem__(self, index):
        if index < self.size:
            return self.A[index]
        else:
            raise IndexError(
                "Index out of range: The provided index is not valid for this list."
            )

    def insert(self, index, ele):
        if self.size == self.n:
            self.resize(1)
        for i in range(self.n, index, -1):
            self.A[i] = self.A[i - 1]
        self.n = self.n + 1
        self.A[index] = ele

    def __delitem__(self, index):
        if 0 <= index < self.n:
            for i in range(index, self.n - 1, +1):
                self.A[i] = self.A[i + 1]
            self.n = self.n - 1
        else:
            raise IndexError(
                "Index out of range: The provided index is not valid for this list."
            )

    def remove(self, ele):
        index = self.find(ele)
        self.__delitem__(index)


L = myArray()
L.append(0)
L.append(1)
L.append(2)
L.append(3)
L.append(4)
L.append(5)
L.append(6)
L.append(7)
L.append(8)
L.append(9)
print(L)
del L[9]
print(L)
