def solution():
    # Calculate the daily earnings from the swimming pool
    kid_price = 3
    adult_price = 2 * kid_price
    daily_earnings = (8 * kid_price) + (10 * adult_price)

    # Calculate the weekly earnings from the swimming pool
    weekly_earnings = daily_earnings * 7
    result = weekly_earnings
    return result

print(solution())