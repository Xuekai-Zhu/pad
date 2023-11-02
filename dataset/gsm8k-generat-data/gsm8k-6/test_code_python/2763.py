def solution():
    # Calculate the total number of boxes sold over three days
    friday_sales = 30
    saturday_sales = friday_sales * 2
    sunday_sales = saturday_sales - 15
    total_sales = friday_sales + saturday_sales + sunday_sales
    result = total_sales
    return result

print(solution())