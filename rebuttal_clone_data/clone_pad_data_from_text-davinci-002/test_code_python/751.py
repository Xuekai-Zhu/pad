def solution():
    monday_speed = 10
    increase_percentage_1 = 50
    increase_percentage_2 = 60
    speed_increase_1 = monday_speed * (increase_percentage_1 / 100)
    speed_increase_2 = speed_increase_1 * (increase_percentage_2 / 100)
    speed_on_friday = speed_increase_1 + speed_increase_2 + monday_speed
    result = speed_on_friday
    
    return result

print(solution())