def solution():
    """Jimmy is setting up a garden. He has three plots: one plot for green beans, one plot for carrots, and one plot for corn. Each corn plant produces 5 times as many servings of veggies as each carrot, and each green bean plant produces half as many servings as each corn plant. If each carrot produces 4 servings of vegetables, and each plot has 9 plants, how many servings of vegetables is Jimmy growing?"""
    carrot_servings = 4
    corn_servings_per_carrot = 5
    green_bean_servings_per_corn = 0.5
    plants_per_plot = 9

    corn_servings = carrot_servings * corn_servings_per_carrot

    green_bean_servings = corn_servings * green_bean_servings_per_corn

    total_servings = (carrot_servings + corn_servings + green_bean_servings) * plants_per_plot * 3

    result = total_servings
    return result

print(solution())