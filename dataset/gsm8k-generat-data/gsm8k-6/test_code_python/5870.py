def solution():
    # Calculate the amount of money made from selling oranges in a year
    oranges_harvests_per_year = 12 // 2  # 12 months in a year, harvest every 2 months
    oranges_money_per_year = oranges_harvests_per_year * 50 

    # Calculate the amount of money made from selling apples in a year
    apples_harvests_per_year = 12 // 3  # 12 months in a year, harvest every 3 months
    apples_money_per_year = apples_harvests_per_year * 30

    # Calculate the total amount of money made in a year
    total_money_per_year = oranges_money_per_year + apples_money_per_year
    result = total_money_per_year
    return result

print(solution())