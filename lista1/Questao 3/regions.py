import numpy as np
from sklearn.utils import shuffle
import random
from math import sqrt

def region_c1(n):
    points = []
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1 - x)
        points.append([x, y, 0])
    return points

def region_c2(n):
    points = []
    for i in range(n):
        x = random.uniform(-1, 0)
        y = random.uniform(0, x + 1)
        points.append([x, y, 1])
    return points

def region_c3(n):
    points = []
    for i in range(n):
        x = random.uniform(-1, 0)
        y = random.uniform(-1-x, 0)
        points.append([x, y, 2])
    return points

def region_c4(n):
    points = []
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(-1+x, 0)
        points.append([x, y, 3])
    return points

def region_c5(n):
    points = []
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(1 - x, sqrt(1 - x**2))
        points.append([x, y, 4])
    return points

def region_c6(n):
    points = []
    for i in range(n):
        x = random.uniform(-1, 0)
        y = random.uniform(x+1, sqrt(1 - x**2))
        points.append([x, y, 5])
    return points

def region_c7(n):
    points = []
    for i in range(n):
        x = random.uniform(-1, 0)
        y = random.uniform(-sqrt(1 - x**2), -1-x)
        points.append([x, y, 6])
    return points

def region_c8(n):
    points = []
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(-sqrt(1 - x**2), -1+x)
        points.append([x, y, 7])
    return points

def entire_region(n):
    points = region_c1(n) + region_c2(n) + region_c3(n) + region_c4(n) + region_c5(n) + region_c6(n) + region_c7(n) + region_c8(n)
    return points
