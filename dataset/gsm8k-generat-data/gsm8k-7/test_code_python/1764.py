def solution():
    season_days = 213

    # Calculate the total number of fish caught by the first fisherman
    fisherman1_rate = 3
    total_fisherman1 = fisherman1_rate * season_days

    # Calculate the total number of fish caught by the second fisherman
    fisherman2_rate_1 = 1
    fisherman2_rate_2 = 2
    fisherman2_rate_3 = 4

    days_rate_1 = 30
    days_rate_2 = 60
    days_rate_3 = season_days - days_rate_1 - days_rate_2

    total_fisherman2 = (
        fisherman2_rate_1 * days_rate_1
        + fisherman2_rate_2 * days_rate_2
        + fisherman2_rate_3 * days_rate_3
    )

    # Calculate the difference in the number of fish caught
    difference = abs(total_fisherman1 - total_fisherman2)
    result = difference
    return result

print(solution())