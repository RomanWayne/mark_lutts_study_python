class Indexer:
    def __getitem__(self, index):
        return index**2


X = Indexer()
print(X[2])


class Stepper:
    def __getitem__(self, index):
        return self.data[index]


X = Stepper()
X.data = 'HUETA'
for item in X:
    print(item)
print('---------------------------------')

class IterExample:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

for i in IterExample(1,9):
    print(i)

I = iter(IterExample(1,7))
print(next(I))
print('---------------------------------')

class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        print('get[%s]:' % i, end='')
        return self.data[i]

    def __iter__(self):
        print('iter =>', end='')
        self.ix = 0
        return self

    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):
        print('contains: ', end='')
        return x in self.data

    def __getattr__(self, i):
        if i == 'whatisclass':
            return self.__class__
        else:
            raise AttributeError('ты че мудак? нет такого атрибута:' + i)
    def __call__(self, *args, **kwargs):
        print('Called: ' , args, kwargs)

X = Iters([0, 1, 2, 3, 4, 6, 8, 9])
print(3 in X)
for i in X:
    print(i, end=' | ')
print()
print([i**2 for i in X])
print(list(map(bin, X)))
print(X.whatisclass)
X(12,3, k = 2, c =7)