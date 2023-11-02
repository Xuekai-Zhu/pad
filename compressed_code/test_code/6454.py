def solution():
    
    max_added_sugar = 150
    soft_drink_calories = 2500
    soft_drink_added_sugar = soft_drink_calories * 0.05
    candy_added_sugar = max_added_sugar * 2 - soft_drink_added_sugar
    bars_of_candy = candy_added_sugar / 25
    result = bars_of_candy
    return result

print(solution())