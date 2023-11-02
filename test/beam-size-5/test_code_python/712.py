def solution():
    
    cheese_weight = 2
    egg_size = 6
    egg_calories = 75 * egg_size
    cheese_calories_per_ounce = 120
    cheese_calories_total = cheese_weight * egg_calories * cheese_calories_per_ounce
    ham_calories_total = ham_weight * 40
    total_calories = cheese_calories_total + ham_calories_total
    result = total_calories
    return result

print(solution())