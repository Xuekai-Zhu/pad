def solution():
    
    thursday_sales = 210
    friday_sales = 2 * thursday_sales
    saturday_sales = 130
    sunday_sales = 0.5 * saturday_sales
    total_sales = thursday_sales + friday_sales + saturday_sales + sunday_sales
    meat_sold_beyond_plans = total_sales - 500
    result = meat_sold_beyond_plans
    return result

print(solution())