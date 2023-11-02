def solution():
    kids_price = 3
    adults_price = 2 * kids_price
    num_kids = 8
    num_adults = 10
    num_days = 7

    # Calculate the total earnings per day from kids and adults
    total_earnings_per_day = (kids_price * num_kids) + (adults_price * num_adults)

    # Calculate the total earnings per week
    total_earnings_per_week = total_earnings_per_day * num_days
    result = total_earnings_per_week
    return result

print(solution())