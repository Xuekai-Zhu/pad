def solution():
    """Haruto has tomato plants in his backyard. This year the plants grew 127 tomatoes. Birds had eaten 19 of the tomatoes. He picked the rest. If Haruto gave half of his tomatoes to his friend, how many tomatoes does he have left?"""
    total_tomatoes = 127
    eaten_tomatoes = 19
    harvested_tomatoes = total_tomatoes - eaten_tomatoes
    given_tomatoes = harvested_tomatoes / 2
    remaining_tomatoes = harvested_tomatoes - given_tomatoes
    result = remaining_tomatoes
    return result

print(solution())