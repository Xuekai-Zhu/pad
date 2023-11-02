def solution():
    normal_cost = 5
    special_cost = 6
    trendy_cost = 8
    normal_haircuts_per_day = 5
    special_haircuts_per_day = 3
    trendy_haircuts_per_day = 2
    days_per_week = 7

    # Calculate the daily earnings from all types of haircuts
    normal_earnings = normal_haircuts_per_day * normal_cost
    special_earnings = special_haircuts_per_day * special_cost
    trendy_earnings = trendy_haircuts_per_day * trendy_cost

    # Calculate the total weekly earnings
    weekly_earnings = (normal_earnings + special_earnings + trendy_earnings) * days_per_week
    result = weekly_earnings
    return result

print(solution())