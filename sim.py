import numpy as np
import vpython as v
from cal import *


class ObjectClass(BaseObjectClass):
    def __init__(self, pos: np.ndarray, mass: float, r: float, velocity: np.ndarray, name: str):
        pos = pos.astype(np.float)
        velocity = velocity.astype(np.float)
        super(ObjectClass, self).__init__(pos, mass, r, velocity, name)
        self.obj = v.sphere(pos=v.vector(*pos), radius=r)

    def set_pos(self, pos):
        v.rate(1000)
        self.obj.pos = v.vector(*pos)


class Env(Environment):
    def add(self, pos, mass, radius, name, velocity: np.ndarray = None):
        if name not in self.objects:
            self.objects[name] = self.type(pos, mass, radius, velocity, name)
            return
        else:
            return 'This name has already been used'


env = Env(3, 0.01, ObjectClass)
print(env.add(np.array([0, 0, 0]), 10**12, 10, 'name', np.array([1, -3, 1])))
print(env.add(np.array([30, 30, 30]), 10**12, 10, 'name2', np.array([-2, -3, 10])))

while True:
    env.run()
