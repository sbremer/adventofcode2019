import aoc

from aoc19_simon.common.intcode import run_intcode

day = 5
lines = aoc.get_input(day)

data_org = [int(code) for code in lines[0].split(',')]

data_out, output = run_intcode(data_org, [1])

result = output[-1]

correct = aoc.submit(result, day)
print(f'Answer 1 correct: {correct}')

data_out, output = run_intcode(data_org, [5])

result2 = output[-1]

correct = aoc.submit(result2, day, 2)
print(f'Answer 2 correct: {correct}')
