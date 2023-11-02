def solution():
    surface_temperature_sunlit = -4
    surface_temperature_shadowed = -112
    required_temperature_for_coat = 0  # This is a placeholder value, you may adjust it based on personal preference
    if surface_temperature_shadowed <= required_temperature_for_coat <= surface_temperature_sunlit:
        result = "maybe"
    elif required_temperature_for_coat < surface_temperature_shadowed:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())