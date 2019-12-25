import aoc

from aoc19_simon.common.processor import Processor

day = 9
lines = aoc.get_input(day)
programm = [int(code) for code in lines[0].split(',')]

proc = Processor(programm)
result = proc.run(1)

correct = aoc.submit(result[0], day)
print(f'Answer 1 correct: {correct}')

proc = Processor(programm)
result = proc.run(2)

correct = aoc.submit(result[0], day, 2)
print(f'Answer 2 correct: {correct}')
