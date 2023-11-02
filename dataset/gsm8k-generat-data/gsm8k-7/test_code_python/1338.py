def solution():
    num_medium_lights = 12

    num_small_lights = num_medium_lights + 10
    num_small_bulbs = num_small_lights

    num_large_lights = num_medium_lights * 2
    num_large_bulbs = num_large_lights * 3

    num_medium_bulbs = num_medium_lights * 2

    # Calculate the total number of bulbs needed
    total_bulbs = num_small_bulbs + num_medium_bulbs + num_large_bulbs
    result = total_bulbs
    return result

print(solution())