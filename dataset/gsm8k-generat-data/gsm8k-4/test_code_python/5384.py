def solution():
    """An apple tree produced 200 apples in a particular season. The tree made 20% fewer fruits the following season, but the tree fruit production in the second season doubled during the third season. Calculate the total number of fruits the apple tree grew in the three seasons."""
    # Define the initial number of apples produced in the first season
    season_1_apples = 200

    # Calculate the number of apples produced in the second season (20% fewer than the first season)
    season_2_apples = season_1_apples * 0.8

    # Calculate the number of apples produced in the third season (double the production of the second season)
    season_3_apples = season_2_apples * 2

    # Calculate the total number of apples produced in the three seasons
    total_apples = season_1_apples + season_2_apples + season_3_apples

    # return the result
    result = total_apples
    return result

print(solution())