def solution():
    race_distance = 2.5 * 200
    electric_car_range = 390
    if race_distance > electric_car_range:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())