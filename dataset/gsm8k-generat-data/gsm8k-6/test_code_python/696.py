def solution():
    # Calculate the number of apples Buffy stole from Carla
    starting_apples = 79  # number of apples Carla puts in her backpack
    lost_apples = 26  # number of apples that fell out of the backpack
    remaining_apples = 8  # number of apples Carla had left at lunchtime
    stolen_apples = starting_apples - remaining_apples - lost_apples
    result = stolen_apples
    return result

print(solution())