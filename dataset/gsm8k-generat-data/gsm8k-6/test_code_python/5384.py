def solution():
    # Calculate the number of apples produced in the second season
    season_2_apples = 0.8 * 200  # 20% fewer fruits than the first season
    # Calculate the number of apples produced in the third season
    season_3_apples = 2 * season_2_apples  # doubled production compared to the second season
    # Calculate the total number of apples produced in the three seasons
    total_apples = 200 + season_2_apples + season_3_apples
    result = total_apples
    return result

print(solution())