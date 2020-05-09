import numpy as np


G = 6.67384e-11


def cal_squared_distance(pos1, pos2):
    return np.sum((pos1-pos2)**2)


def cal_size_of_ga(mass1, mass2, squared_d):
    c = G/squared_d
    return mass2*c, mass1*c


def normalize(vec, magnitude):
    return vec / magnitude


def cal_a(pos1, pos2, a1, a2, squared_d):
    pos = pos2 - pos1
    distance = np.sqrt(squared_d)
    n = normalize(pos, distance)
    return n * a1, -n * a2


def cal(pos1, pos2, mass1, mass2):
    sq_d = cal_squared_distance(pos1, pos2)
    ga = cal_size_of_ga(mass1, mass2, sq_d)
    return cal_a(pos1, pos2, *ga, sq_d)


def cal_displacement(velocity, dt):
    return velocity*dt

