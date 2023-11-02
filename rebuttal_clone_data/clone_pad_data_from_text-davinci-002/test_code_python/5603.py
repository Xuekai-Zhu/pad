def solution():
    speed = 150
    percent_increase_1 = 30
    percent_increase_2 = 15
    speed_increase_1 = speed * (percent_increase_1 / 100)
    speed_increase_2 = speed_increase_1 * (percent_increase_2 / 100)
    new_speed = speed + speed_increase_1 + speed_increase_2
    result = new_speed
    return result

print(solution())