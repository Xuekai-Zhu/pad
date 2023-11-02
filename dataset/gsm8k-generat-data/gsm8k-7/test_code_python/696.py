def solution():
    starting_apples = 79
    lost_apples = 26
    remaining_apples = 8

    # Calculate the total number of apples that Carla had before Buffy and the hole incident
    total_apples = starting_apples - lost_apples

    # Calculate the number of apples that Buffy stole
    num_stolen_apples = total_apples - remaining_apples
    result = num_stolen_apples
    return result

print(solution())