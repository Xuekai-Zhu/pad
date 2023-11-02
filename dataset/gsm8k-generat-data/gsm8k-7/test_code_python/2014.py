def solution():
    num_tanks_with_heater = 3
    num_fish_per_tank_with_heater = 15

    num_fish_left = 75 - (num_tanks_with_heater * num_fish_per_tank_with_heater)

    num_tanks_needed = num_fish_left // 10
    if num_fish_left % 10 != 0:
        num_tanks_needed += 1

    result = num_tanks_needed
    return result

print(solution())