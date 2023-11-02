def solution():
    # Calculate the total number of servings needed for the girls
    servings_for_girls = 1.5 * 3

    # Add servings for Willow's son
    total_servings = servings_for_girls + 3

    # Calculate the total number of single pancakes needed
    single_pancakes = total_servings * 4

    result = single_pancakes
    return result

print(solution())