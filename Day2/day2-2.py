from copy import deepcopy
from Day2.day2 import calculate_result, load_code, UnknownOpcode


def main():
    code = load_code()
    for noun in range(100):
        for verb in range(100):
            code_copy = deepcopy(code)
            code_copy[1] = noun
            code_copy[2] = verb
            try:
                if calculate_result(code_copy) == 19690720:
                    print(100 * noun + verb)
                    break
            except UnknownOpcode:
                pass


if __name__ == '__main__':
    main()
