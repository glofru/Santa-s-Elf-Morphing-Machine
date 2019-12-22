#!/usr/bin/python

'''
lambda^2 - Tr*lambda + Det = 0
D = M_inv*A*M ==>   A = M*D*M_inv
18 decimal digits needed
'''

import numpy
from decimal import *
getcontext().prec = 18



with open('trans.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

NUM_OF_LINES = len(lines)
M = numpy.array([[1., 0.],[0.,1.]])

A_matrices = []

for i in range(0, NUM_OF_LINES, 4):
    det = float(lines[i]) #parsing data to get determinant
    trace = float(lines[i+1]) #parsing data to get trace
    # print(det)
    # print(trace)

    poly = [1, -trace, det]
    lambdas = numpy.roots(poly) #resolve characteristic polynomial to get eigenvalues
    lambdas = numpy.sort(lambdas)[::-1] #invert the list

    D = numpy.array([[float(lambdas[0]), 0],[0, float(lambdas[1])]]) #diagonal matrix of eigenvalues

    line2 = lines[i+2]
    line3 = lines[i+3]
    
    M11 = float(line2[3:line2[3:].find(" ")+3]) #parsing of the modal matrix
    M12 = float(line2[line2[3:].find(" ")+3:line2.find("]")])
    M21 = float(line3[line3.find("[")+1:line3[2:].find(" ")+2])
    M22 = float(line3[line3[2:].find(" ")+2:line3.find("]]")])
    M = numpy.array([[M11, M12],[M21, M22]])
    M_inv = numpy.linalg.inv(M) #invert modal matrix

    MD = numpy.matmul(M, D) #product among matrices
    A = numpy.matmul(MD, M_inv)

    A_matrices.append(A)



base_elf = numpy.array([1, 3])
nth_elf = base_elf
for matrix in A_matrices:
    # print(matrix)
    nth_elf = matrix.dot(nth_elf)
    nth_elf[0] = round(nth_elf[0])
    nth_elf[1] = round(nth_elf[1])
    print(nth_elf) #all the points
