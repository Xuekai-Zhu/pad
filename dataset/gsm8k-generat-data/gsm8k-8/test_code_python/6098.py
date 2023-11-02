def solution():
    # Define Matt's speed
    matt_speed = 20

    # Define Tom's speed as 5 steps per minute more than Matt's speed
    tom_speed = matt_speed + 5

    # Calculate the number of steps Matt has gone up so far
    matt_steps = 220

    # Calculate the time it took Matt to reach 220 steps
    matt_time = matt_steps / matt_speed

    # Calculate how many steps Tom will have gone up in the same amount of time
    tom_steps = tom_speed * matt_time
    result = tom_steps
    return result

print(solution())