with open('input.txt', 'r') as f:
    print(sum(map(lambda x: x//3 - 2, map(int, f.readlines()))))
