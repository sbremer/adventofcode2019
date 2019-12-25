from typing import List, Tuple, Dict, Callable


def run_intcode(data: List[int], input_int: int = None) -> Tuple[List[int], List[int]]:
    at = 0

    output = []

    def get_param(always_immediate: bool = False) -> int:
        nonlocal at

        if p1_mode == 1 or always_immediate:
            p1 = data[at + 1]
        elif p1_mode == 0:
            p1 = data[data[at + 1]]
        else:
            raise ValueError(f'Unknown parameter mode: {p1_mode}')

        at += 2

        return p1

    def get_params_2() -> Tuple[int, int]:
        nonlocal at

        if p1_mode == 0:
            p1 = data[data[at + 1]]
        elif p1_mode == 1:
            p1 = data[at + 1]
        else:
            raise ValueError(f'Unknown parameter mode: {p1_mode}')

        if p2_mode == 0:
            p2 = data[data[at + 2]]
        elif p2_mode == 1:
            p2 = data[at + 2]
        else:
            raise ValueError(f'Unknown parameter mode: {p2_mode}')

        at += 3

        return p1, p2

    def get_params_3() -> Tuple[int, int, int]:
        nonlocal at

        if p1_mode == 0:
            p1 = data[data[at + 1]]
        elif p1_mode == 1:
            p1 = data[at + 1]
        else:
            raise ValueError(f'Unknown parameter mode: {p1_mode}')

        if p2_mode == 0:
            p2 = data[data[at + 2]]
        elif p2_mode == 1:
            p2 = data[at + 2]
        else:
            raise ValueError(f'Unknown parameter mode: {p2_mode}')

        pos_result = data[at + 3]

        at += 4

        return p1, p2, pos_result

    def opt_1():
        p1, p2, pos_result = get_params_3()
        data[pos_result] = p1 + p2

    def opt_2():
        p1, p2, pos_result = get_params_3()
        data[pos_result] = p1 * p2

    def opt_3():
        p1 = get_param(True)
        data[p1] = input_int

    def opt_4():
        p1 = get_param()
        output.append(p1)

    def opt_5():
        nonlocal at

        p1, p2 = get_params_2()
        if p1 != 0:
            at = p2

    def opt_6():
        nonlocal at

        p1, p2 = get_params_2()
        if p1 == 0:
            at = p2

    def opt_7():
        p1, p2, pos_result = get_params_3()
        if p1 < p2:
            data[pos_result] = 1
        else:
            data[pos_result] = 0

    def opt_8():
        p1, p2, pos_result = get_params_3()
        if p1 == p2:
            data[pos_result] = 1
        else:
            data[pos_result] = 0

    opt_codes: Dict[int, Callable] = {
        1: opt_1,
        2: opt_2,
        3: opt_3,
        4: opt_4,
        5: opt_5,
        6: opt_6,
        7: opt_7,
        8: opt_8,
    }

    while data[at] != 99:
        opt_raw = data[at]
        opt = opt_raw % 100
        p1_mode = (opt_raw // 100) % 10
        p2_mode = (opt_raw // 1000) % 10
        p3_mode = (opt_raw // 10000) % 10

        if opt in opt_codes.keys():
            opt_func = opt_codes[opt]
            opt_func()
        else:
            raise ValueError(f'Unknown opt code: {opt} at position {at}!')

    return data, output
