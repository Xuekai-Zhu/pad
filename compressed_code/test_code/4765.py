def solution():
    
    meal1_price, meal1_count = 8, 10
    meal2_price, meal2_count = 10, 5
    meal3_price, meal3_count = 4, 20
    total_sales = (meal1_price * meal1_count) + (meal2_price * meal2_count) + (meal3_price * meal3_count)
    result = total_sales
    return result

print(solution())