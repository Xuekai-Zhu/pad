def solution():
    total_days = 30
    days_left = total_days * (1 - 4/5)  # Calculate the remaining days
    pills_left = 12
    pills_per_day = pills_left / days_left  # Calculate the pills per day
    result = pills_per_day
    return result

print(solution())