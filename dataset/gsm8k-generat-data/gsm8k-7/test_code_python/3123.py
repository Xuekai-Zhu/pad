def solution():
    water_per_bottle = 12
    num_refills = 7
    total_water = water_per_bottle * num_refills

    needed_water = 100
    remaining_water = needed_water - total_water
    result = remaining_water
    return result

print(solution())