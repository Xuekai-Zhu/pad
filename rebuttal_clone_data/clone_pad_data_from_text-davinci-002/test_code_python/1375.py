def solution():
    pig_birth = 6
    month_12 = 3
    month_16 = 3
    pig_sold_12 = month_12 * 300
    pig_sold_16 = month_16 * 300
    food_12 = month_12 * 10
    food_16 = (month_16 - month_12) * 10
    total_food = food_12 + food_16
    total_profit = pig_sold_12 + pig_sold_16 - total_food
    result = total_profit
    
    return result

print(solution())