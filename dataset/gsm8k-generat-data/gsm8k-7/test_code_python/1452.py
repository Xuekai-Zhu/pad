def solution():
    distance = 1000
    abel_speed = 50
    alice_speed = 40
    time_difference = 1/6  # 1 hour difference in decimal form
    total_time_difference = distance / (abel_speed - alice_speed)  # in hours
    time_in_minutes = (total_time_difference - time_difference) * 60  # in minutes
    result = time_in_minutes
    return result

print(solution())