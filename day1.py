#!/usr/bin/env python3

import math

vectors = []

def calc_fuel(mass):
    return math.floor(mass / 3) - 2

def calc_fuel_recursive(mass):
    fuel = calc_fuel(mass)
    if calc_fuel(fuel) > 0:
        fuel = fuel + calc_fuel_recursive(fuel)

    return fuel

with open('day1.txt') as fp:
    while True:
        line = fp.readline()
        if line is None or line == '':
            break

        vectors.append( int(line.strip()) )

sum = 0
for v in vectors:
    sum += calc_fuel(v)

print("Part 1 sum: %d" % (sum))

sum = 0
for v in vectors:
    sum += calc_fuel_recursive(v)

print("Part 2 sum: %d" % (sum))
