def solution():
    
    medium_lights = 12
    small_lights = medium_lights + 10
    large_lights = medium_lights * 2
    bulbs_per_small_light = 1
    bulbs_per_medium_light = 2
    bulbs_per_large_light = 3
    total_bulbs = (small_lights * bulbs_per_small_light) + (medium_lights * bulbs_per_medium_light) + (large_lights * bulbs_per_large_light)
    result = total_bulbs
    return result

print(solution())