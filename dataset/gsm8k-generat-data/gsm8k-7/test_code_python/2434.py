def solution():
    friday_sales = 40
    saturday_sales = (2 * friday_sales) - 10
    sunday_sales = friday_sales / 2

    # Calculate the total sales for all three days
    total_sales = friday_sales + saturday_sales + sunday_sales
    result = total_sales
    return result

print(solution())