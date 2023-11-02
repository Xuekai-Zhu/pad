def solution():
    # Define the number of medium ceiling lights and the corresponding bulbs needed
    medium_lights = 12
    medium_bulbs = 2

    # Calculate the number of small and large ceiling lights based on the given information
    small_lights = medium_lights + 10
    large_lights = 2 * medium_lights

    # Calculate the total number of bulbs needed
    total_bulbs = medium_lights * medium_bulbs + small_lights + large_lights * 3
    result = total_bulbs
    return result

print(solution())