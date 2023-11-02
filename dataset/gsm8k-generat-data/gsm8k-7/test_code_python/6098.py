def solution():
    matt_speed = 20
    tom_speed = matt_speed + 5
    matt_steps = 220

    # Calculate the time it takes for Matt to reach 220 steps
    matt_time = matt_steps / matt_speed

    # Calculate the number of steps Tom will have gone up in the same time
    tom_steps = tom_speed * matt_time

    result = tom_steps
    return result

print(solution())