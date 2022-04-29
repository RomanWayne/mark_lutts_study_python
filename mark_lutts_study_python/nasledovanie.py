class Super:
    def method(self):
        print('in Super.method')     # Поведение по умолчанию
    def delegate(self):
        self.action()               #Ожидаемый метод (пример абстрактного класса)
                                    #т.е. ожидается что метод будет реализован в наследнике
    def action(self):
        assert False, 'action must be defined'

class Inheritor(Super):             # Наследует методы, как они есть
    pass


class Replacer(Super): # Полностью замещает method
    def method(self):
        print('in Replacer.method')


class Extender(Super): # Расширяет поведение метода method
    def method(self):
        print('start Extender.method')
        Super.method(self)
        print('end Extender.method')


class Provider(Super): # Определяет необходимый метод
    def action(self):
        print('in Provider.method')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider')
    x = Provider()
    x.delegate()