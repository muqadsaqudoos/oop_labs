class Numbers:
    def __init__(self, *elements):
        self.elements = list(elements)
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.elements):
            a = self.elements[self.index]
            self.index += 1
            return a
        else:
            raise StopIteration

    def addTheNumberInList(self, a):
        self.elements.append(a)
        self.updateOddEvenList()
        return self.elements

    def searchNumberInList(self, a):
        if a in self.elements:
            return f"{a} does exist in list"
        else:
            return f"{a} does not exist in list"

    def delElementinList(self, a):
        if a in self.elements:
            self.elements.remove(a)
            self.updateOddEvenList()
            return self.elements

    def alterElementWithNewElement(self, index, newElement):
        if index<len(self.elements):
            self.elements[index] = newElement
            self.updateOddEvenList()
            return self.elements

    def updateOddEvenList(self):
        self.odd = [x for x in self.elements if x % 2 != 0]
        self.even = [x for x in self.elements if x % 2 == 0]

    def __getitem__(self, index):
        if  index < len(self.elements):
            return self.elements[index]

    def __setitem__(self, index, value):
        if index < len(self.elements):
            self.elements[index] = value
            self.updateOddEvenList()
        

def main():
    nums = Numbers(1, 2, 3, 4, 5, 6, 7)
    print(f"Adding the number in List:")
    print(nums.addTheNumberInList(8))
    print(f"\nSearching the number in List:")
    print(nums.searchNumberInList(4))
    print(f"\nDeleting the number in List:")
    print(nums.delElementinList(1))
    print(f"\nAltering the Element with new Element:")
    print(nums.alterElementWithNewElement(4,89))
    print("\n")
    for x in nums:
        print(x)
    print(f"\nOdd list:")
    print(nums.odd)
    print(f"\nEven list")
    print(nums.even)

main()
