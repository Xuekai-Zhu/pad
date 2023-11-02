def solution():
    initial_weight = 50000
    first_unload_percentage = 0.1
    second_unload_percentage = 0.2

    # Calculate the weight after the first unloading
    weight_after_first_unload = initial_weight - (initial_weight * first_unload_percentage)

    # Calculate the weight after the second unloading
    weight_after_second_unload = weight_after_first_unload - (weight_after_first_unload * second_unload_percentage)

    result = weight_after_second_unload
    return result

print(solution())