def solution():
    price_8inch = 5
    price_16inch = 2 * price_8inch

    num_8inch_daily = 3
    num_16inch_daily = 5

    num_days = 3

    # Calculate the total earnings per day from selling 8-inch portraits
    earnings_8inch_daily = num_8inch_daily * price_8inch

    # Calculate the total earnings per day from selling 16-inch portraits
    earnings_16inch_daily = num_16inch_daily * price_16inch

    # Calculate the total earnings per day
    total_earnings_daily = earnings_8inch_daily + earnings_16inch_daily

    # Calculate the total earnings over 3 days
    total_earnings = total_earnings_daily * num_days
    result = total_earnings
    return result

print(solution())