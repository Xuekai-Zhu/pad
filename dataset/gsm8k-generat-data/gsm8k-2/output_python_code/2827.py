def solution():
    """Adam has 18 magnets. He gave away a third of the magnets, and he still had half as many magnets as Peter. How many magnets does Peter have?"""
    adam_magnets = 18
    peter_magnets = 2 * (adam_magnets - (1/3 * adam_magnets))
    result = peter_magnets
    return result

print(solution())