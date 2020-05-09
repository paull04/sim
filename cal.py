from abc import abstractmethod
from collections import deque
from dataclasses import dataclass
import numpy as np
import func as f


@dataclass
class BaseObjectClass:
    pos: np.ndarray
    mass: float
    radius: float
    velocity: np.ndarray
    name: str

    def update_pos(self, dt):
        self.pos += f.cal_displacement(self.velocity, dt)
        self.set_pos(self.pos)

    @abstractmethod
    def set_pos(self, pos):
        pass


class Environment:
    def __init__(self, d, dt, t: type):
        self.dt = dt
        self.type = t
        self.d = d
        self.objects = {}

    @staticmethod
    def __cal(obj1, objects):
        for obj2 in objects:
            a = f.cal(obj1.pos, obj2.pos, obj1.mass, obj2.mass)
            obj1.velocity += a[0]
            obj2.velocity += a[1]

    def run(self):
        objects = deque(self.objects.values())
        while objects:
            obj1 = objects.pop()
            self.__cal(obj1, objects)
            obj1.update_pos(self.dt)