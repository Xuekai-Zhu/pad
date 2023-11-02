def solution():
    
    thursday_sales = 210
    friday_sales = thursday_sales * 2
    saturday_sales = 130
    sunday_sales = saturday_sales / 2
    
    total_sales = thursday_sales + friday_sales + saturday_sales + sunday_sales
    extra_sales = total_sales - 500
    
    result = extra_sales
    return result

print(solution())