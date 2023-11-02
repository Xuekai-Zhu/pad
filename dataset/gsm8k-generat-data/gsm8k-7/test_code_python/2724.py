def solution():
    num_plants_per_plot = 9

    # Calculate the total number of servings of veggies per plot of carrots
    servings_per_carrot = 4
    total_servings_per_carrot_plot = servings_per_carrot * num_plants_per_plot

    # Calculate the total number of servings of veggies per plot of corn
    servings_per_corn = 5 * servings_per_carrot
    total_servings_per_corn_plot = servings_per_corn * num_plants_per_plot

    # Calculate the total number of servings of veggies per plot of green beans
    servings_per_green_bean = servings_per_corn / 2
    total_servings_per_green_bean_plot = servings_per_green_bean * num_plants_per_plot

    # Calculate the total number of servings of veggies across all three plots
    total_servings = total_servings_per_carrot_plot + total_servings_per_corn_plot + total_servings_per_green_bean_plot
    result = total_servings
    return result

print(solution())