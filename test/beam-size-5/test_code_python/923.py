def solution():
    
    cinnamon_rolls = 200
    blueberry_muffins = 300
    normal_cinnamon_calories = 600
    normal_blueberry_muffin_calories = 450
    pastry_calories = (normal_cinnamon_rolls * normal_cinnamon_calories) / 3
    total_calories = pastry_calories * pastry_calories
    result = total_calories
    return result

print(solution())