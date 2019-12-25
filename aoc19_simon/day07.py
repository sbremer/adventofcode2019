from typing import List
from itertools import permutations

import aoc

from aoc19_simon.common.intcode import run_intcode


def run_amps(phases: List[int], int_prog: List[int]) -> int:
    control_in = 0
    for amp in range(5):
        input_ints = [phases[amp], control_in]
        _, outputs = run_intcode(int_prog, input_ints)
        control_in = outputs[0]

    return control_in


day = 7
lines = aoc.get_input(day)

int_prog = [int(code) for code in lines[0].split(',')]

thurst_max = 0
phases_max = None

for phases in permutations(range(5)):
    thurst = run_amps(phases, int_prog)
    if thurst > thurst_max:
        thurst_max = thurst
        phases_max = phases

result = thurst_max

correct = aoc.submit(result, day)
print(f'Answer 1 correct: {correct}')
