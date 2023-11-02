def solution():
    daily_pastries = 20
    daily_bread = 10
    pastry_price = 2
    bread_price = 4

    # Calculate the total sales for today
    today_sales = (14 * pastry_price) + (25 * bread_price)

    # Calculate the daily average sales
    daily_avg_sales = (daily_pastries * pastry_price) + (daily_bread * bread_price)

    # Calculate the difference between daily average and today's sales
    diff = daily_avg_sales - today_sales
    result = diff
    return result

print(solution())