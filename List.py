class List(list):
    def __getitem__(self, key):
        if isinstance(key, int):
            return super().__getitem__(key % len(self))
        elif isinstance(key, slice):
            if key.start is None and key.stop is None:
                return super().__getitem__(slice(key.start, key.stop, key.step))
            if key.start is None:
                return super().__getitem__(slice(key.start, key.stop % len(self), key.step))
            if key.stop is None:
                return super().__getitem__(slice(key.start % len(self), key.stop, key.step))

            return super().__getitem__(slice(key.start % len(self), key.stop % len(self), key.step)) or \
                super().__getitem__(slice(key.stop % len(self), key.start % len(self), key.step))

if __name__ == '__main__':
    l = List([1,2,3,4,5,5,6,7,8])
    l.append(9)
    print(l[::2])