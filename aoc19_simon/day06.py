import aoc

day = 6
lines = aoc.get_input(day)

orbits = {}

for line in lines:
    orbit_center, orbiter = line.split(')')

    orbits[orbiter] = orbit_center

indirect = 0

for item in orbits.keys():

    to_com = 0
    parent = orbits[item]
    while parent != 'COM':
        parent = orbits[parent]
        to_com += 1

    indirect += to_com

result = len(orbits) + indirect


correct = aoc.submit(result, day)
print(f'Answer 1 correct: {correct}')

at_you = 'YOU'
at_san = 'SAN'
parents_you = {}
parents_san = {}
at = 0

while at_you not in parents_san.keys() and at_san not in parents_you.keys():
    at_you = orbits[at_you]
    at_san = orbits[at_san]
    parents_you[at_you] = at
    parents_san[at_san] = at
    at += 1

if at_you in parents_san.keys():
    result2 = parents_you[at_you] + parents_san[at_you]
else:
    result2 = parents_you[at_san] + parents_san[at_san]


correct = aoc.submit(result2, day, 2)
print(f'Answer 2 correct: {correct}')
