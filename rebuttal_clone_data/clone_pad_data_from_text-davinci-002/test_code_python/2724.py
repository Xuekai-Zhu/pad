def solution():
    carrot_servings = 4
    corn_servings = carrot_servings * 5
    green_bean_servings = corn_servings / 2
    plants_per_plot = 9
    carrot_plot_servings = carrot_servings * plants_per_plot
    corn_plot_servings = corn_servings * plants_per_plot
    green_bean_plot_servings = green_bean_servings * plants_per_plot
    total_servings = carrot_plot_servings + corn_plot_servings + green_bean_plot_servings
    result = total_servings
    return result

print(solution())