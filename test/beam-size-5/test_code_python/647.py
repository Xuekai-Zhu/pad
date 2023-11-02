def solution():
    
    red_sales = 400
    green_sales = red_sales / 2
    first_month_sales = red_sales + green_sales
    second_month_sales = (3/4) * first_month_sales
    total_sales = first_month_sales + second_month_sales
    result = total_sales
    return result

print(solution())