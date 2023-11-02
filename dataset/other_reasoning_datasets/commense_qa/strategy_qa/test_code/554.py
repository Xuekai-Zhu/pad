def solution():
    can_use_oven_to_dehydrate = True
    can_use_sunlight_and_heat_to_dry = True
    if can_use_oven_to_dehydrate or can_use_sunlight_and_heat_to_dry:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())