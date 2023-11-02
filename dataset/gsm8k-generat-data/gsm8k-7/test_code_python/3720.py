def solution():
    pastry_price = 5
    days_per_week = 7
    first_day_sales = 2
    total_sales = 0

    # Calculate the total number of pastries sold in the week
    for i in range(days_per_week):
        total_sales += first_day_sales + i

    # Calculate the average daily sales
    average_sales = total_sales / days_per_week
    result = average_sales
    return result

print(solution())