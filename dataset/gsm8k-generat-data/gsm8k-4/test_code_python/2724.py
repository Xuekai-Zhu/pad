def solution():
    """Jimmy is setting up a garden. He has three plots: one plot for green beans, one plot for carrots, and one plot for corn. Each corn plant produces 5 times as many servings of veggies as each carrot, and each green bean plant produces half as many servings as each corn plant. If each carrot produces 4 servings of vegetables, and each plot has 9 plants, how many servings of vegetables is Jimmy growing?"""
    # Define the number of plants per plot
    plants_per_plot = 9

    # Define the number of servings per carrot
    servings_per_carrot = 4

    # Calculate the number of servings per corn
    servings_per_corn = servings_per_carrot * 5

    # Calculate the number of servings per green bean
    servings_per_greenbean = servings_per_corn / 2

    # Calculate the total number of servings
    total_servings = (plants_per_plot * servings_per_carrot) + (plants_per_plot * servings_per_corn) + (plants_per_plot * servings_per_greenbean)

    # return the result
    result = total_servings
    return result

print(solution())