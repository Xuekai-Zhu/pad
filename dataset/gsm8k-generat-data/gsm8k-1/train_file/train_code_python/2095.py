def solution():
    """Beth went shopping. She bought 15 more cans of peas than twice the number of cans of corn that she bought. If she bought 35 cans of peas, how many cans of corn did she buy?"""
    peas = 35
    peas_formula = peas - 15
    corn = peas_formula / 2
    result = corn
    return result

print(solution())