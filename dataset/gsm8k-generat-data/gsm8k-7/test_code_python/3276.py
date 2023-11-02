def solution():
    final_speed = 188
    subtraction_value = 4

    # Undo the last step: double and subtract 4
    speed_after_subtraction = final_speed / 2 - subtraction_value

    # Undo doubling the speed
    rabbit_speed = speed_after_subtraction / 2
    result = rabbit_speed
    return result

print(solution())