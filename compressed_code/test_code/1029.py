def solution():
    
    medium_lights = 12
    small_lights = medium_lights + 10
    large_lights = 2 * medium_lights
    total_bulbs = (medium_lights * 2) + small_lights + (large_lights * 3)
    result = total_bulbs
    return result

print(solution())