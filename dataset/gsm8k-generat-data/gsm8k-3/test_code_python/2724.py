def solution():
    """Jimmy is setting up a garden. He has three plots: one plot for green beans, one plot for carrots, and one plot for corn. Each corn plant produces 5 times as many servings of veggies as each carrot, and each green bean plant produces half as many servings as each corn plant. If each carrot produces 4 servings of vegetables, and each plot has 9 plants, how many servings of vegetables is Jimmy growing?"""
    # Define the number of plants in each plot and the servings produced by each carrot
    plants_per_plot = 9
    servings_per_carrot = 4

    # Calculate the servings produced by each corn plant and each green bean plant
    servings_per_corn = servings_per_carrot * 5
    servings_per_green_bean = servings_per_corn / 2

    # Calculate the total servings produced by each plot
    servings_per_carrot_plot = servings_per_carrot * plants_per_plot
    servings_per_corn_plot = servings_per_corn * plants_per_plot
    servings_per_green_bean_plot = servings_per_green_bean * plants_per_plot

    # Calculate the total servings produced by all three plots
    total_servings = servings_per_carrot_plot + servings_per_corn_plot + servings_per_green_bean_plot

    # Display the total servings
    result = total_servings
    return result

print(solution())