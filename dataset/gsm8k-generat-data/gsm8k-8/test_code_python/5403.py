def solution():
    # Calculate the total battery life in hours
    total_battery_life = 60

    # Calculate the remaining battery life after using 3/4 of it
    remaining_battery = total_battery_life * (1 - 3/4)

    # Calculate the battery life remaining after the 2-hour math exam
    battery_after_exam = remaining_battery - 2

    result = battery_after_exam
    return result

print(solution())