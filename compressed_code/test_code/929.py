def solution():
    
    apple_price = 1.5
    orange_price = 1
    morning_apples = 40
    morning_oranges = 30
    afternoon_apples = 50
    afternoon_oranges = 40
    morning_sales = (apple_price * morning_apples) + (orange_price * morning_oranges)
    afternoon_sales = (apple_price * afternoon_apples) + (orange_price * afternoon_oranges)
    total_sales = morning_sales + afternoon_sales
    result = total_sales
    return result

print(solution())