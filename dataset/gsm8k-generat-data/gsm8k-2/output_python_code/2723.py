def solution():
    """Jimmy is setting up a garden. He has three plots: one plot for green beans, one plot for carrots, and one plot for corn. Each corn plant produces 5 times as many servings of veggies as each carrot, and each green bean plant produces half as many servings as each corn plant. If each carrot produces 4 servings of vegetables, and each plot has 9 plants, how many servings of vegetables is Jimmy growing?"""
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