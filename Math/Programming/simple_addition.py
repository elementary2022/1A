#!/usr/bin/env python3

from random import randint
from sys import argv
from os import linesep

def run(group, problems, reference):
    z = [[randint(0, 20) for y in range(2)] for x in range(4 * group)]
    alpha = [z[x: x + 4] for x in range(0, len(z), 4)]
    problem = open(problems, 'w')
    for y in alpha:
        problem.write('{{{}}} + {{{}}} &= \\underline{{\hspace{{1cm}}}} & {{{}}} + {{{}}} &= \\underline{{\hspace{{1cm}}}} & {{{}}} + {{{}}} &= \\underline{{\hspace{{1cm}}}} & {{{}}} + {{{}}} &= \\underline{{\hspace{{1cm}}}} \\\\'.format(
            y[0][0], y[0][1], y[1][0], y[1][1], y[2][0], y[2][1], y[3][0], y[3][1]))
        problem.write(linesep)
    _file = problem.name
    problem.close()
    print('tex block generated to {}'.format(_file))
    reference = open(reference, 'w')
    for y in alpha:
        reference.write('{{{}}} + {{{}}} &= {{{}}} & {{{}}} + {{{}}} &= {{{}}} & {{{}}} + {{{}}} &= {{{}}} & {{{}}} + {{{}}} &= {{{}}} \\\\'.format(
            y[0][0], y[0][1], y[0][0] + y[0][1], y[1][0], y[1][1], y[1][0] + y[1][1], y[2][0], y[2][1], y[2][0] + y[2][1], y[3][0], y[3][1], y[3][0] + y[3][1]))
        reference.write(linesep)
    _file = reference.name
    reference.close()
    print('tex block generated to {}'.format(_file))

if __name__ == '__main__':
    if len(argv) < 4:
        exit()
    group = 8
    if argv[1].isdigit():
        group = int(argv[1])
    run(group, argv[2], argv[3])
