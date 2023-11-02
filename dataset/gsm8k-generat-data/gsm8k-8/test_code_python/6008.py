def solution():
    # Calculate the total number of crabs Tom catches per day
    crabs_per_bucket = 12
    total_crabs_per_day = crabs_per_bucket * 8

    # Calculate Tom's daily earnings from selling crabs
    crab_price = 5
    daily_earnings = total_crabs_per_day * crab_price

    # Calculate Tom's weekly earnings
    days_per_week = 7
    weekly_earnings = daily_earnings * days_per_week
    result = weekly_earnings
    return result

print(solution())