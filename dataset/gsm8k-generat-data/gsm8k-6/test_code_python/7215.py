def solution():
    # Calculate the total sales for the baker's daily average
    daily_average = 20 * 2 + 10 * 4  # 20 pastries sold for $2 and 10 loaves of bread sold for $4

    # Calculate the total sales for today
    today_sales = 14 * 2 + 25 * 4  # 14 pastries sold for $2 and 25 loaves of bread sold for $4

    # Calculate the difference in sales
    difference = today_sales - daily_average
    result = difference
    return result

print(solution())