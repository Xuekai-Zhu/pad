def solution():
    weekday_price = 18  # The price of a haircut on a weekday is $18
    weekend_price = weekday_price * 1.5  # Haircuts cost 50% more on weekends

    # Calculate how much Mario would have paid the day before his last haircut
    price_on_weekend = weekend_price
    result = price_on_weekend
    return result

print(solution())