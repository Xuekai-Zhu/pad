def solution():
    # Define cactus watering needs based on weather
    hot_weather = True
    if hot_weather:
        cactus_needs_water = True
    else:
        cactus_needs_water = False

    # Check if cactus soil should always be damp
    if cactus_needs_water:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())