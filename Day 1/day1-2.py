def calc_fuel(mass):
    if mass == 0:
        return 0
    next_mass = max(0, mass//3 - 2)
    return calc_fuel(next_mass) + next_mass


with open('input.txt', 'r') as f:
    print(sum(map(calc_fuel, map(int, f.readlines()))))
