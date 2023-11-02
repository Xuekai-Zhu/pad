def solution():
    initial_speed = 80  # Jon's initial fastball speed
    training_weeks = 4 * 4  # Jon goes through training 4 times for 4 weeks each time
    speed_gain = 0.2  # Jon increases his speed by 20%

    # Calculate Jon's final fastball speed
    final_speed = initial_speed * (1 + speed_gain)

    # Calculate the average weekly speed gain
    weekly_speed_gain = (final_speed - initial_speed) / training_weeks
    result = weekly_speed_gain
    return result

print(solution())