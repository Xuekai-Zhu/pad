def solution():
    # Define the initial load and the percentages
    initial_load = 50000
    first_unload_percentage = 0.1
    second_unload_percentage = 0.2

    # Calculate the weight unloaded at the first stop
    first_unload = initial_load * first_unload_percentage

    # Calculate the weight remaining after the first stop
    remaining_load_after_first = initial_load - first_unload

    # Calculate the weight unloaded at the second stop
    second_unload = remaining_load_after_first * second_unload_percentage

    # Calculate the final weight left on the truck
    final_weight_left = remaining_load_after_first - second_unload
    result = final_weight_left
    return result

print(solution())