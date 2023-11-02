def solution():
    green_car = 1
    red_car = green_car * 2
    blue_car = green_car / 8
    speed_blue_car = 80
    speed_green_car = speed_blue_car * blue_car
    speed_red_car = speed_green_car * red_car
    result = speed_red_car
    return result

print(solution())