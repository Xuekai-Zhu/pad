def solution():
    # Define the amount of sugar for the first layer
    sugar_first_layer = 2

    # Define the size of the second layer in relation to the first
    size_second_layer = 2
    
    # Define the size of the third layer in relation to the second
    size_third_layer = 3
    
    # Calculate the amount of sugar for the second layer
    sugar_second_layer = sugar_first_layer * size_second_layer
    
    # Calculate the amount of sugar for the third layer
    sugar_third_layer = sugar_second_layer * size_third_layer
    
    result = sugar_third_layer
    return result

print(solution())