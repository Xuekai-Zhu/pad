def solution():
    num_plants = 9  # Each plot has 9 plants
    servings_per_carrot = 4  # Each carrot produces 4 servings of veggies
    servings_per_corn = servings_per_carrot * 5  # Each corn plant produces 5 times as many servings as each carrot
    servings_per_green_bean = servings_per_corn / 2  # Each green bean plant produces half as many servings as each corn plant

    # Calculate the total number of servings from each plot
    total_servings_carrots = num_plants * servings_per_carrot
    total_servings_corn = num_plants * servings_per_corn
    total_servings_green_beans = num_plants * servings_per_green_bean

    # Calculate the total number of servings from all three plots
    total_servings = total_servings_carrots + total_servings_corn + total_servings_green_beans
    result = total_servings
    return result

print(solution())