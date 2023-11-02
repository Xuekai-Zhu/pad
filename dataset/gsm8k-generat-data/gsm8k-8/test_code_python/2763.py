def solution():
    # Calculate the number of boxes sold on each day
    friday_sales = 30
    saturday_sales = 2 * friday_sales
    sunday_sales = saturday_sales - 15

    # Calculate the total sales over the three days
    total_sales = friday_sales + saturday_sales + sunday_sales
    result = total_sales
    return result

print(solution())