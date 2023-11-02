def solution():
    first_day_sales = 14
    second_day_sales = 25
    third_day_sales = first_day_sales * 2
    fourth_day_sales = third_day_sales * 2
    total_sales = first_day_sales + second_day_sales + third_day_sales + fourth_day_sales
    result = total_sales
    return result

print(solution())