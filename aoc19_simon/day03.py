import numpy as np

import aoc

directions = {
    'U': np.array([0, 1]),
    'D': np.array([0, -1]),
    'R': np.array([1, 0]),
    'L': np.array([-1, 0])
}

day = 3
lines = aoc.get_input(day)

cable1 = [(inst[0], int(inst[1:])) for inst in lines[0].split(',')]
cable2 = [(inst[0], int(inst[1:])) for inst in lines[1].split(',')]

grid = {}
at = np.array([0, 0])
step = 0

for direction, length in cable1:
    delta = directions[direction]
    for _ in range(length):
        at += delta
        step += 1
        if at.tostring() not in grid.keys():
            grid[at.tostring()] = step


min_dist = 1e100
min_at = None

min_delay = 1e100
min_delay_at = None

at = np.array([0, 0])
step = 0

for direction, length in cable2:
    delta = directions[direction]
    for _ in range(length):
        at += delta
        step += 1
        if at.tostring() in grid.keys():
            dist = np.abs(at).sum()
            if dist < min_dist:
                min_dist = dist
                min_at = at

            delay = step + grid[at.tostring()]
            if delay < min_delay:
                min_delay = delay
                min_delay_at = at

print(min_dist)

correct = aoc.submit(min_dist, day)
print(f'Answer 1 correct: {correct}')

print(min_delay)

correct = aoc.submit(min_delay, day, 2)
print(f'Answer 2 correct: {correct}')
