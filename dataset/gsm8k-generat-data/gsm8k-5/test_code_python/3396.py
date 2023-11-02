def solution():
    remy_sales = 55  # Remy sold 55 bottles of soda in the morning
    nick_sales = remy_sales - 6  # Nick sold six fewer bottles of soda than Remy
    price_per_bottle = 0.5  # The price per bottle is $.50

    # Calculate the total sales in the morning
    morning_sales = remy_sales * price_per_bottle

    # Calculate the total sales in the evening
    evening_sales = (remy_sales + nick_sales) * price_per_bottle

    # Calculate the difference between evening and morning sales
    difference = evening_sales - morning_sales
    result = difference
    return result

print(solution())