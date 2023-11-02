def solution():
    # Calculate the total amount of money made during high season
    high_season_sales = 6 * 15 * 60  # 6 packs of tuna fish are sold per hour during peak season, for 15 hours

    # Calculate the total amount of money made during low season
    low_season_sales = 4 * 15 * 60  # 4 packs of tuna fish are sold per hour during low season, for 15 hours

    # Calculate the difference in money made between high and low season
    difference = high_season_sales - low_season_sales

    result = difference
    return result

print(solution())