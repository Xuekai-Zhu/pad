def solution():
    num_houses = 30
    matchsticks_per_house = 10

    # Calculate the total number of matchsticks used
    total_matchsticks_used = num_houses * matchsticks_per_house

    # Calculate the total number of matchsticks Michael originally had
    original_matchsticks = total_matchsticks_used * 2
    result = original_matchsticks
    return result

print(solution())