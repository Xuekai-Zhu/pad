def solution():
    # Calculate the total number of goats as the difference between the total number of animals and the number of cows and sheep
    total_animals = 200
    cows = 40
    sheep = 56
    goats = total_animals - cows - sheep
    result = goats
    return result

print(solution())