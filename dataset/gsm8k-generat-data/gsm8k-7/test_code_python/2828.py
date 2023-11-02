def solution():
    initial_magnets = 18
    given_away = initial_magnets / 3
    remaining = initial_magnets - given_away
    peter_magnets = remaining * 2
    result = peter_magnets
    return result

print(solution())