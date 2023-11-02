def solution():
    """Adam has 18 magnets. He gave away a third of the magnets, and he still had half as many magnets as Peter. How many magnets does Peter have?"""
    adam_magnets = 18
    adam_gave_away = adam_magnets // 3
    peter_magnets = (adam_magnets - adam_gave_away) * 2
    result = peter_magnets
    return result

print(solution())