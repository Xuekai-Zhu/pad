def solution():
    # Calculate the total servings from the carrot plot
    carrot_servings = 4 * 9

    # Calculate the total servings from the corn plot
    corn_servings = 5 * 4 * 9

    # Calculate the total servings from the green bean plot
    green_bean_servings = 0.5 * 5 * 4 * 9

    # Calculate the total servings from all plots
    total_servings = carrot_servings + corn_servings + green_bean_servings
    result = total_servings
    return result

print(solution())