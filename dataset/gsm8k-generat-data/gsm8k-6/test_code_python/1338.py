def solution():
    # Calculate the total number of bulbs needed
    medium_lights = 12
    small_lights = medium_lights + 10
    large_lights = 2 * medium_lights

    total_bulbs = (2 * medium_lights) + (1 * small_lights) + (3 * large_lights)

    result = total_bulbs
    return result

print(solution())