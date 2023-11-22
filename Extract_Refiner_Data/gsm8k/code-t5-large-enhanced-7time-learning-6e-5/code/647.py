def solution():
    
    red_sales = 400
    green_sales = red_sales / 2
    second_month_sales = (3/4) * (red_sales + green_sales)
    total_sales = red_sales + green_sales + second_month_sales
    result = total_sales
    return result

print(solution())