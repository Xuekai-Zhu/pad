def solution():
    # Calculate the amount of sugar needed for the third layer
    sugar_for_first_layer = 2
    sugar_for_second_layer = 2 * 2  # second layer is twice as big as the first layer
    sugar_for_third_layer = 2 * 2 * 3  # third layer is three times larger than the second layer
    total_sugar = sugar_for_third_layer
    result = total_sugar
    return result

print(solution())