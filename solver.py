#!/usr/bin/python

'''
lambda^2 - Tr*lambda + Det = 0
D = M_inv*A*M ==>   A = M*D*M_inv
'''

import numpy
import matplotlib.pyplot as plt

with open('trans.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

NUM_OF_LINES = len(lines)

M = numpy.array([[1., 0.],[0.,1.]])
A_matrices = []
elves = []

for i in range(0, NUM_OF_LINES, 4):
    det = float(lines[i].split(' ', 1)[1])
    trace = float(lines[i+1].split(' ', 1)[1])

    poly = [1, -trace, det]
    lambdas = numpy.roots(poly)
    lambdas = numpy.sort(lambdas)[::-1]

    D = numpy.array([[float(lambdas[0]), 0],[0, float(lambdas[1])]])

    line2 = lines[i+2]
    line3 = lines[i+3]

    M11 = float(line2[line2.find("[[")+2:line2.find(" ")])
    M12 = float(line2[line2.find(" ")+1:line2.find("]")])
    M21 = float(line3[line3.find("[")+1:line3.find(" ")])
    M22 = float(line3[line3.find(" ")+1:line3.find("]]")])
    M = numpy.array([[M11, M12],[M21, M22]])
    M_inv = numpy.linalg.inv(M)

    MD = numpy.matmul(M, D)
    A = numpy.matmul(MD, M_inv)

    A_matrices.append(A)



base_elf = numpy.array([1, 3])
elves.append(base_elf)

nth_elf = base_elf
for matrix in A_matrices:
    nth_elf = matrix.dot(nth_elf)
    nth_elf[0] = round(nth_elf[0])
    nth_elf[1] = round(nth_elf[1])
    print(nth_elf)
    elves.append(nth_elf)

data = numpy.array(elves)

x , y = data.T
plt.scatter(x, y, s=6)
plt.show()