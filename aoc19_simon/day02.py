from typing import List

import aoc

day = 2
lines = aoc.get_input(day)


def run_intcode(data: List[int]) -> int:
    at = 0

    while data[at] != 99:
        opt = data[at]
        pos1 = data[at + 1]
        pos2 = data[at + 2]
        pos_result = data[at + 3]

        if opt == 1:
            data[pos_result] = data[pos1] + data[pos2]
        elif opt == 2:
            data[pos_result] = data[pos1] * data[pos2]
        else:
            print(f'Unknown opt code: {opt}!')
            break

        at += 4

    return data[0]


data_org = [int(code) for code in lines[0].split(',')]

data = data_org.copy()
data[1] = 12
data[2] = 2

result = run_intcode(data)

correct = aoc.submit(result, day)
print(f'Answer 1 correct: {correct}')

result2 = None
for noun in range(99):
    for verb in range(99):

        data = data_org.copy()
        data[1] = noun
        data[2] = verb

        output = run_intcode(data)

        if output == 19690720:
            result2 = 100*noun + verb
            break

if result2 is not None:
    correct = aoc.submit(result2, day, 2)
    print(f'Answer 2 correct: {correct}')
else:
    print('No valid input found for given output!')
