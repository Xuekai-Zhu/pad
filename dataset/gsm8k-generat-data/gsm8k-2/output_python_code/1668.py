def solution():
    """In a field where there are 200 animals, there are 40 cows, 56 sheep and goats. How many goats are there?"""
    total_animals = 200
    cows = 40
    sheep = 56
    goats = total_animals - cows - sheep
    result = goats
    return result

print(solution())