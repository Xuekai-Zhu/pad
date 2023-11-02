def solution():
    matt_speed = 20  # Matt goes up the stairs 20 steps per minute
    tom_speed = matt_speed + 5  # Tom goes up the stairs 5 steps per minute more than Matt
    matt_steps = 220  # Matt has reached 220 steps above the entrance

    # Calculate the time it took Matt to reach 220 steps
    matt_time = matt_steps / matt_speed

    # Calculate the number of steps Tom will have gone up by that time
    tom_steps = tom_speed * matt_time

    result = tom_steps
    return result

print(solution())