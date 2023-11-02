def solution():
    friday_sales = 30
    saturday_sales = friday_sales * 2
    sunday_sales = saturday_sales - 15

    # Calculate the total sales over three days
    total_sales = friday_sales + saturday_sales + sunday_sales
    result = total_sales
    return result

print(solution())