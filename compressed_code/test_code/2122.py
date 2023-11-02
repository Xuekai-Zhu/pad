def solution():
    
    carrot_servings = 4
    corn_servings = 5 * carrot_servings
    green_bean_servings = 0.5 * corn_servings
    plants_per_plot = 9
    total_carrot_servings = carrot_servings * plants_per_plot
    total_corn_servings = corn_servings * plants_per_plot
    total_green_bean_servings = green_bean_servings * plants_per_plot
    total_servings = total_carrot_servings + total_corn_servings + total_green_bean_servings
    result = total_servings
    return result

print(solution())