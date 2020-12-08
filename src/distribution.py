from math import e, floor, log
from random import random


def rand(a, b) -> float:
    return a + (b - a) * random()


def ber(p):
    return 1 if random() < p else 0


def exponential(lam: float) -> float:
    return 1 - e ** (-lam * random())


def exponentialX(lam: float, x: float) -> float:
    return 1 - e ** (-lam * x)


def mean(value):
    return sum(value) / len(value)
