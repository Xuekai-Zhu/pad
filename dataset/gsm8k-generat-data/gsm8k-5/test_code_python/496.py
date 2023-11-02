def solution():
    houses = 30  # Michael creates 30 matchsticks houses
    matchsticks_per_house = 10  # Each house uses 10 matchsticks
    matchsticks_used = houses * matchsticks_per_house  # Total number of matchsticks used
    matchsticks_original = matchsticks_used * 2  # Michael used only half of his original pile of matchsticks

    result = matchsticks_original
    return result

print(solution())