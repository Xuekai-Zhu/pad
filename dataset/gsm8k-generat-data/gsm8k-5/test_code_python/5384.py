def solution():
    # Number of apples in the first season
    season_one = 200

    # Number of apples in the second season (20% fewer than the first season)
    season_two = season_one - (season_one * 0.20)

    # Number of apples in the third season (double the second season)
    season_three = season_two * 2

    # Total number of apples in all three seasons
    total_apples = season_one + season_two + season_three
    result = total_apples
    return result

print(solution())