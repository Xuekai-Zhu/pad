def solution():
    fine_per_mile = 16
    total_fine = 256
    speed_limit = 50
    speeding_speed = total_fine / fine_per_mile + speed_limit
    result = speeding_speed
    return result

print(solution())