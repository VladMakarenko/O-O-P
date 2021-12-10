from abc import ABC, abstractmethod

class material(ABC):

    t_p = 1538 # плавится
    t_i = 2862 # испаряется

    def draw(self):
        print('...')


class Iron(material):
    def agg_state(self, t):
        if t >= self.t_p and t <= self.t_i:
            print("Расплавился")
        elif t < self.t_p:
            print("Замерз\затвердел")
        else:
            print("Испарился")

a = Iron()
print(a.draw())
print(a.agg_state(1537))