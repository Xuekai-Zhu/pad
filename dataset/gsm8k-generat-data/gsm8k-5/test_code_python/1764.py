def solution():
    season_days = 213  # Number of days in the Cod fishing season
    total_fish_fisherman1 = 3 * season_days  # Total fish caught by the first fisherman who catches at a steady rate of 3 per day

    # Total fish caught by the second fisherman who starts slowly and then catches more fish later
    total_fish_fisherman2 = 30 * 1 + 60 * 2 + (season_days - 90) * 4

    # Calculate the difference in the total number of fish caught by both fishermen
    fish_difference = abs(total_fish_fisherman1 - total_fish_fisherman2)
    result = fish_difference
    return result

print(solution())