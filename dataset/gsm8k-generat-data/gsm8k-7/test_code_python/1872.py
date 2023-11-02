def solution():
    num_birds = 20
    jim_to_disney_distance = 50
    disney_to_london_distance = 60

    # Calculate the distance traveled by all the birds in the first season
    total_distance_season_1 = num_birds * jim_to_disney_distance

    # Calculate the distance traveled by all the birds in the second season
    total_distance_season_2 = num_birds * disney_to_london_distance

    # Calculate the combined distance traveled by all the birds in the two seasons
    total_distance = total_distance_season_1 + total_distance_season_2
    result = total_distance
    return result

print(solution())