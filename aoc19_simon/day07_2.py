from typing import List
from itertools import permutations

import aoc

from aoc19_simon.common.processor import Processor


day = 7
lines = aoc.get_input(day)

int_prog = [int(code) for code in lines[0].split(',')]


def run_amps(phases: List[int]) -> int:
    amps: List[Processor] = []

    for i in range(5):
        amp = Processor(int_prog)
        amp.run_with_input(phases[i])
        amps.append(amp)

    var = 0
    while True:
        for i in range(5):
            var_new = amps[i].run_till_output(var)
            if var_new is None:
                break
            var = var_new

        if var_new is None:
            break
    return var


thurst_max = 0
phases_max = None

for phases in permutations(range(5, 10)):
    thurst = run_amps(phases)
    if thurst > thurst_max:
        thurst_max = thurst
        phases_max = phases

result2 = thurst_max

correct = aoc.submit(result2, day, 2)
print(f'Answer 2 correct: {correct}')
