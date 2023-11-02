def solution():
    remy_sales = 55
    nick_sales = remy_sales - 6
    price_per_bottle = 0.5
    total_sales = 55

    # Calculate the total revenue from morning sales
    morning_revenue = remy_sales * price_per_bottle

    # Calculate the total revenue from evening sales
    evening_revenue = total_sales - morning_revenue

    # Calculate the difference in earnings between evening and morning sales
    difference_in_earnings = evening_revenue - morning_revenue
    result = difference_in_earnings
    return result

print(solution())