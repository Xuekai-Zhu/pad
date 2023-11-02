def solution():
    
    morning_apples = 40
    morning_oranges = 30
    afternoon_apples = 50
    afternoon_oranges = 40
    price_apples = 1.50
    price_oranges = 1
    total_sales = (morning_apples + afternoon_apples) * price_apples + (morning_oranges + afternoon_oranges) * price_oranges
    result = total_sales
    return result

print(solution())