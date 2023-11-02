def solution():
    
    friday_sales = 30
    saturday_sales = 2 * friday_sales
    sunday_sales = saturday_sales - 15
    total_sales = friday_sales + saturday_sales + sunday_sales
    result = total_sales
    return result

print(solution())