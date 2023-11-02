def solution():
    
    first_day_sales = 45
    second_day_sales = first_day_sales + 20
    third_day_sales = (2 * second_day_sales) - 10
    total_sales = 350
    fourth_day_sales = total_sales - (first_day_sales + second_day_sales + third_day_sales)
    result = fourth_day_sales
    return result

print(solution())