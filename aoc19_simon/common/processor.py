from typing import List, Tuple, Dict, Callable

from collections import defaultdict


class Processor:
    def __init__(self, program: List[int]):
        data = {i: d for i, d in enumerate(program)}
        self.data = defaultdict(int, data)
        self.at = 0
        self.opt = 0
        self.p_mode = [-1, -1, -1]
        self.input = None
        self.base = 0

        self.opt_codes: Dict[int, Callable] = {
            1: self.opt_1,
            2: self.opt_2,
            3: self.opt_3,
            4: self.opt_4,
            5: self.opt_5,
            6: self.opt_6,
            7: self.opt_7,
            8: self.opt_8,
            9: self.opt_9,
        }

    def get_address(self, p_at: int = 0) -> int:
        if self.p_mode[p_at] == 0:
            p_addr = self.data[self.at]
        elif self.p_mode[p_at] == 2:
            p_addr = self.data[self.at] + self.base
        else:
            raise ValueError(f'Unknown parameter mode: {self.p_mode[p_at]}')

        self.at += 1

        return p_addr

    def get_param(self, p_at: int = 0) -> int:
        if self.p_mode[p_at] == 0:
            p1 = self.data[self.data[self.at]]
        elif self.p_mode[p_at] == 1:
            p1 = self.data[self.at]
        elif self.p_mode[p_at] == 2:
            p1 = self.data[self.data[self.at] + self.base]
        else:
            raise ValueError(f'Unknown parameter mode: {self.p1_mode}')

        self.at += 1

        return p1

    def get_params_2(self) -> Tuple[int, int]:

        if self.p_mode[0] == 0:
            p1 = self.data[self.data[self.at]]
        elif self.p_mode[0] == 1:
            p1 = self.data[self.at]
        elif self.p_mode[0] == 2:
            p1 = self.data[self.data[self.at] + self.base]
        else:
            raise ValueError(f'Unknown parameter mode: {self.p1_mode}')

        if self.p_mode[1] == 0:
            p2 = self.data[self.data[self.at + 1]]
        elif self.p_mode[1] == 1:
            p2 = self.data[self.at + 1]
        elif self.p_mode[1] == 2:
            p2 = self.data[self.data[self.at + 1] + self.base]
        else:
            raise ValueError(f'Unknown parameter mode: {self.p_mode[1] }')

        self.at += 2

        return p1, p2

    def get_params_3(self) -> Tuple[int, int, int]:
        p1, p2 = self.get_params_2()
        pos_result = self.get_address(2)

        return p1, p2, pos_result

    def opt_1(self):
        p1, p2, pos_result = self.get_params_3()
        self.data[pos_result] = p1 + p2

    def opt_2(self):
        p1, p2, pos_result = self.get_params_3()
        self.data[pos_result] = p1 * p2

    def opt_3(self):
        p1 = self.get_address()
        self.data[p1] = self.input

    def opt_4(self):
        p1 = self.get_param()
        return p1

    def opt_5(self):
        p1, p2 = self.get_params_2()
        if p1 != 0:
            self.at = p2

    def opt_6(self):
        p1, p2 = self.get_params_2()
        if p1 == 0:
            self.at = p2

    def opt_7(self):
        p1, p2, pos_result = self.get_params_3()
        if p1 < p2:
            self.data[pos_result] = 1
        else:
            self.data[pos_result] = 0

    def opt_8(self):
        p1, p2, pos_result = self.get_params_3()
        if p1 == p2:
            self.data[pos_result] = 1
        else:
            self.data[pos_result] = 0

    def opt_9(self):
        p1 = self.get_param()
        self.base += p1

    def get_opt(self):
        opt_raw = self.data[self.at]
        self.opt = opt_raw % 100
        self.p_mode[0] = (opt_raw // 100) % 10
        self.p_mode[1] = (opt_raw // 1000) % 10
        self.p_mode[2] = (opt_raw // 10000) % 10
        self.at += 1

    def run_step(self):
        self.get_opt()

        if self.opt in self.opt_codes.keys():
            opt_func = self.opt_codes[self.opt]
            output = opt_func()
        elif self.opt == 99:
            return None
        else:
            raise ValueError(f'Unknown opt code: {self.opt} at position {self.at}!')

        return output

    def run_with_input(self, input_int: int):

        self.input = input_int

        while True:
            self.run_step()
            if self.opt == 3 or self.opt == 99:
                break

    def run_till_output(self, input_int: int = None):
        self.input = input_int

        while True:
            result = self.run_step()
            if result is not None or self.opt == 99:
                break

        return result

    def run(self, input_int: int = None) -> List[int]:
        self.input = input_int

        output = []

        while True:
            result = self.run_step()
            if result is not None:
                output.append(result)
            if self.opt == 99:
                break

        return output
