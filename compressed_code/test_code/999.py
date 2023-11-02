def solution():
    
    first_week_sales = 35
    second_week_sales = first_week_sales * 2
    third_week_sales = first_week_sales * 3
    total_sales = first_week_sales + second_week_sales + third_week_sales
    commission = total_sales * 1
    salary = 500
    bonus = 50
    total_earnings = commission + salary + bonus
    result = total_earnings
    return result

print(solution())