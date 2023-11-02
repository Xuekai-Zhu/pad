def solution():
    # Calculate the weight of the load remaining after the two deliveries
    first_unload = 0.1 * 50000
    remaining_load_1 = 50000 - first_unload
    second_unload = 0.2 * remaining_load_1
    remaining_load_2 = remaining_load_1 - second_unload
    result = remaining_load_2
    return result

print(solution())