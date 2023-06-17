class List(list):
    def __getitem__(self, key):
        return super().__getitem__(key % len(self))

if __name__ == '__main__':
    l = List([1,2,3,4,5,5,6,6,7,8])
    print(l[-10000])