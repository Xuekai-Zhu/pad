def solution():
    hours_of_sleep = 6
    increase = 1 / 3
    new_hours_of_sleep = hours_of_sleep + (hours_of_sleep * increase)
    result = new_hours_of_sleep
    return result

print(solution())