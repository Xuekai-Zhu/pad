def solution():
    # Define variables for Burning Man weather conditions
    hot_summer_sun = True
    shaded_areas = False
    # Determine if people are more likely to get sunburn at Burning Man
    if hot_summer_sun and not shaded_areas:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())