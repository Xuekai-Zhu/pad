def solution():
    weekday_price = 18
    weekend_price = weekday_price * 1.5  # 50% increase

    # Calculate how much Mario would have paid the day before his Monday haircut
    # Assuming Sunday is the day before Monday
    previous_day_price = weekend_price

    result = previous_day_price
    return result

print(solution())