def solution():
    initial_time = 3
    final_time = 3.5
    hours_traveled = final_time - initial_time
    miles_traveled = 448
    speed1 = miles_traveled / hours_traveled
    speed2 = speed1 - 30
    result = speed2
    return result

print(solution())