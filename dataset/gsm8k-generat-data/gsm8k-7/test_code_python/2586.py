def solution():
    keanu_speed = 20
    shark_speed = keanu_speed * 2
    pilot_fish_speed_increment = shark_speed - keanu_speed
    pilot_fish_speed = keanu_speed + (pilot_fish_speed_increment / 2)
    result = pilot_fish_speed
    return result

print(solution())