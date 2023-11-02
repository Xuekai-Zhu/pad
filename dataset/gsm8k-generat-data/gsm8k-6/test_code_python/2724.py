def solution():
    # Calculate the number of servings of vegetables from the carrots
    servings_carrots = 4 * 9  # 4 servings per carrot plant, 9 carrot plants in the plot

    # Calculate the number of servings of vegetables from the corn plants
    servings_corn = (5 * 4) * 9  # 5 times as many servings as each carrot plant, 4 servings per carrot, 9 plants in the plot

    # Calculate the number of servings of vegetables from the green bean plants
    servings_green_beans = 0.5 * (5 * 4) * 9  # 0.5 times as many servings as each corn plant, 5 times as many servings as each carrot, 4 servings per carrot, 9 plants in the plot

    # Calculate the total servings of vegetables
    total_servings = servings_carrots + servings_corn + servings_green_beans
    result = total_servings
    return result

print(solution())