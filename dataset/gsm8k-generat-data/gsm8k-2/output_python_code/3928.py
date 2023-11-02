def solution():
    """Matthew, Patrick and Alvin are eating dinner together. Matthew eats three times as many egg rolls as Patrick eats. Patrick eats half as many egg rolls as Alvin eats. If Alvin ate 4 egg rolls, how many did Matthew eat?"""
    alvin_eats = 4
    patrick_eats = alvin_eats / 2
    matthew_eats = patrick_eats * 3
    result = matthew_eats
    return result

print(solution())