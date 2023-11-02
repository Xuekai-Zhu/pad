def solution():
    """Haruto has tomato plants in his backyard. This year the plants grew 127 tomatoes. Birds had eaten 19 of the tomatoes. He picked the rest. If Haruto gave half of his tomatoes to his friend, how many tomatoes does he have left?"""
    total_tomatoes = 127
    eaten_tomatoes = 19
    remaining_tomatoes = total_tomatoes - eaten_tomatoes
    given_away_tomatoes = remaining_tomatoes / 2
    tomatoes_left = remaining_tomatoes - given_away_tomatoes
    result = tomatoes_left
    return result

print(solution())