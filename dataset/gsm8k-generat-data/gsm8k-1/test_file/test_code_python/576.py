def solution():
    """Maggie's oven is malfunctioning. When she sets it to 450 the actual temperature is 468. If it's off by the same percentage for any recipe, what temperature should she set it at if her recipe calls for 520 degrees?"""
    set_temp = 520
    actual_temp = 468
    percent_difference = (actual_temp - 450) / 450
    adjusted_temp = set_temp * (1 + percent_difference)
    result = adjusted_temp
    return result

print(solution())