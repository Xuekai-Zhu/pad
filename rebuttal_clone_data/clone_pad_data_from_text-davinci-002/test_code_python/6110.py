def solution():
    hours_outside = 8
    cups_per_bottle = 2
    water_drank = hours_outside * cups_per_bottle
    water_used = water_drank + (5 * cups_per_bottle)
    result = water_used
    return result

print(solution())