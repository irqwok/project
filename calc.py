import math
class Calculator:
    def __int__(self, first, second):
        self.first = first
        self.second = second

    def plus(self):
        sum = self.first + self.second
        print(sum)

    def minus(self):
        vidnim = self.first - self.second
        print(vidnim)

    def mnozh(self):
        mnosh = self.first * self.second
        print(mnosh)

    def dil(self):
        if self.second != 0:
            dilen = self.first / self.second
            print(dilen)
        else: print("Дія неможлива!")


    def discr(self, a, b, c):
        d = b**2 - 4*a*c
        if d>0:
            x1 = (-b + math.sqrt(d))/2*a
            x2 = (-b - math.sqrt(d)) / 2 * a
        if d == 0:
            x = b/2*a
        if d<0:
            print("x - порожня множина")

a = Calculator()
a.discr(3,5,2)