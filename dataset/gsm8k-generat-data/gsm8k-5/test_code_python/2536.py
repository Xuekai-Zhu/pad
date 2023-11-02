def solution():
    postcards_per_day = 30  # Tina makes 30 postcards per day
    price_per_postcard = 5  # Tina gets $5 for each postcard sold
    days = 6  # Tina has sold postcards for 6 days

    # Total number of postcards sold
    total_postcards_sold = postcards_per_day * days

    # Total amount of money earned
    total_earned = total_postcards_sold * price_per_postcard
    result = total_earned
    return result

print(solution())