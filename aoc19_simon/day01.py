import aoc

day = 1
lines = aoc.get_input(day)


def get_fuel(mass: int) -> int:
    return mass // 3 - 2


total_fuel = sum([get_fuel(int(line)) for line in lines])

correct = aoc.submit(total_fuel, day)
print(f'Answer correct: {correct}')


def get_fuel_2(mass: int) -> int:
    fuel = mass // 3 - 2
    if fuel < 0:
        return 0

    fuel += get_fuel_2(fuel)

    return fuel


total_fuel_2 = sum([get_fuel_2(int(line)) for line in lines])

correct = aoc.submit(total_fuel_2, day, 2)
print(f'Answer 2 correct: {correct}')
