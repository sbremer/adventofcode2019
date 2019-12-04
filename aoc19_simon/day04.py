import aoc

day = 4
lines = aoc.get_input(day)

depth_total = 6

start, end = map(int, lines[0].split('-'))

candidates = [(0, False)]

for depth in range(1, 7):
    start_depth = start // 10 ** (depth_total - depth)
    end_depth = end // 10 ** (depth_total - depth)
    candidates_next = []

    for candidate in candidates:
        digits, double = candidate
        last_digit = digits % 10
        if depth == 1:
            last_digit = -1

        for digit in range(10):
            digits_new = digits * 10 + digit
            if start_depth <= digits_new <= end_depth and digit >= last_digit:
                candidate_new = (digits_new, last_digit == digit or double)
                candidates_next.append(candidate_new)

    candidates = candidates_next

result = sum([1 for candidate in candidates if candidate[1]])

correct = aoc.submit(result, day)
print(f'Answer 1 correct: {correct}')

candidates = [(0, False, 0)]

for depth in range(1, 7):
    start_depth = start // 10 ** (depth_total - depth)
    end_depth = end // 10 ** (depth_total - depth)
    candidates_next = []

    for candidate in candidates:
        digits, double, streak = candidate
        last_digit = digits % 10
        if depth == 1:
            last_digit = -1

        for digit in range(10):
            digits_new = digits * 10 + digit
            if start_depth <= digits_new <= end_depth and digit >= last_digit:
                streak_new = streak + 1 if last_digit == digit else 1
                double_new = double or (streak_new == 1 and streak == 2)
                candidate_new = (digits_new, double_new, streak_new)
                candidates_next.append(candidate_new)

    candidates = candidates_next

result2 = sum([1 for candidate in candidates if candidate[1] or candidate[2] == 2])

correct = aoc.submit(result2, day, 2)
print(f'Answer 2 correct: {correct}')
