def solution():
    chinese_symbols = ["monkeys", "goats", "tigers"]
    quadruped_animals = ["tigers"]
    overlap = [animal for animal in chinese_symbols if animal in quadruped_animals]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())