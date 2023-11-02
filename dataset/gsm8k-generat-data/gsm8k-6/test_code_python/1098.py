def solution():
    # Calculate the number of watermelons Jeremy has left after giving 2 to his dad each week
    watermelons_left_per_week = 30 - 3 - 2
    weeks_last = watermelons_left_per_week // 5  # 5 watermelons left after giving 2 to his dad each week
    result = weeks_last
    return result

print(solution())