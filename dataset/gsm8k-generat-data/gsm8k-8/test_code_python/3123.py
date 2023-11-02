def solution():
    total_water_bottle_can_hold = 12
    times_water_bottle_refilled = 7

    total_water_consumption = total_water_bottle_can_hold * times_water_bottle_refilled
    water_left_to_drink = 100 - total_water_consumption
    result = water_left_to_drink
    return result

print(solution())