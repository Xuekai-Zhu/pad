def solution():
    max_battery_life = 60  # Brody's calculator can run for 60 hours on a full battery
    current_battery_life = max_battery_life * 0.75  # Brody has used three quarters of the battery
    exam_time = 2  # Brody's exam will take 2 hours

    # Calculate the remaining battery life after the exam
    remaining_battery_life = current_battery_life - exam_time

    result = remaining_battery_life
    return result

print(solution())