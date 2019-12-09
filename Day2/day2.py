from typing import List


class UnknownOpcode(Exception):
    pass


def load_code() -> List[int]:
    with open('input.txt', 'r') as f:
        return list(map(int, f.read().split(',')))


def calculate_result(code: List[int]) -> int:
    for i in range(0, len(code), 4):
        if code[i] == 1:
            code[code[i+3]] = code[code[i+1]] + code[code[i+2]]
        elif code[i] == 2:
            code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
        elif code[i] == 99:
            return code[0]
        else:
            raise UnknownOpcode(f'Unknown opcode: {i} -> {code[i]}')
    return code[0]


def main():
    code = load_code()
    code[1] = 12
    code[2] = 2
    print(calculate_result(code))

if __name__ == '__main__':
    main()
