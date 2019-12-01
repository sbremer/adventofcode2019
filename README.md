## Advent of Code 2019

Have fun! :)

### How to use:
- Fork
- Create your own folder (eg: aoc19_your_name)
- Copy `config.sample.py` to `config.py`
- Open your browser and get the session token through the development console  
(Chrome: F12 -> Application -> Cookies -> session)
- Insert token into your config.py (which is ignored by git)
- Create and run a script per day (eg: `aoc19_your_name/day_01.py`). Example:

```python
import aoc

day = 1
lines = aoc.get_input(day)

answer_1 = magic_1(lines)

correct = aoc.submit(answer_1, day)
print(f'Answer correct: {correct}')

answer_2 = magic_2(lines)

correct = aoc.submit(answer_2, day, 2)
print(f'Answer 2 correct: {correct}')
```

The statement `import aoc` will automatically download the puzzles till today
and make them available through `aoc.get_input(day)`.
