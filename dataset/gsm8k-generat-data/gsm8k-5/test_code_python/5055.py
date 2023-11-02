def solution():
    sugar_first_layer = 2  # The first layer requires 2 cups of sugar
    sugar_second_layer = sugar_first_layer * 2  # The second layer is twice as big as the first
    sugar_third_layer = sugar_second_layer * 3  # The third layer is three times larger than the second

    # Calculate the total cups of sugar needed for the third layer
    total_sugar_third_layer = sugar_third_layer - sugar_second_layer

    result = total_sugar_third_layer
    return result

print(solution())