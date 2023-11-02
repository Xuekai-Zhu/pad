def solution():
    # Calculate Tina's mile time
    tina_time = 6
    tom_speed = 3*tina_time
    tina_speed = 1/3*tom_speed
    tony_speed = 2*tina_speed

    # Calculate the total time for all three runners
    total_time = tina_time + tom_speed + 1/tony_speed

    result = total_time
    return result

print(solution())