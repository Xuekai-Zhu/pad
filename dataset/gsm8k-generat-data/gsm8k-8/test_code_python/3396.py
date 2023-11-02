def solution():
    # Calculate Nick's sales
    nick_sales = (55 - 6) * 0.50

    # Calculate Remy's morning sales
    remy_morning_sales = 55 * 0.50

    # Calculate their total sales for the day
    total_sales = remy_morning_sales + nick_sales + 55

    # Calculate how much more they earned in the evening compared to morning
    evening_earnings = total_sales - (remy_morning_sales + nick_sales)

    result = evening_earnings
    return result

print(solution())