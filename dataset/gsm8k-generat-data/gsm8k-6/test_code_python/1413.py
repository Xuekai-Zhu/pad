def solution():
    # Calculate the earnings from tulips and roses sold on the first day
    earnings_day1 = 30*2 + 20*3  # 30 tulips sold at $2 each and 20 roses sold at $3 each

    # Calculate the earnings from tulips and roses sold on the second day
    earnings_day2 = earnings_day1 * 2  # double the previous day's sales

    # Calculate the earnings from tulips and roses sold on the third day
    earnings_day3 = 0.1*earnings_day2 + 16*3  # 10% of tulips sold on day 2 at $2 each and 16 roses sold at $3 each

    # Calculate the total earnings over the three days
    total_earnings = earnings_day1 + earnings_day2 + earnings_day3

    result = total_earnings
    return result

print(solution())