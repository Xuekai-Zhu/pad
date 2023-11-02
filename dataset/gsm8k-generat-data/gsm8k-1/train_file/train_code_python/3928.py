def solution():
    """Matthew, Patrick and Alvin are eating dinner together. Matthew eats three times as many egg rolls as Patrick eats. Patrick eats half as many egg rolls as Alvin eats. If Alvin ate 4 egg rolls, how many did Matthew eat?"""
    alvin_rolls = 4
    patrick_rolls = alvin_rolls / 2
    matthew_rolls = patrick_rolls * 3
    result = matthew_rolls
    return result

print(solution())