def solution():
    """Matt and Tom both walk up the stairs of the library. Matt goes up the stairs 20 steps per minute. Tom goes up the stairs 5 steps per minute more than Matt. If Matt has reached 220 steps above the entrance, how many steps will Tom have gone up by that time?"""
    # Define Matt's speed and the extra speed of Tom
    MATT_SPEED = 20
    TOM_EXTRA_SPEED = 5

    # Calculate the number of steps Matt has gone up
    matt_steps = 220

    # Calculate the time it took Matt to climb to his current position
    matt_time = matt_steps / MATT_SPEED

    # Calculate Tom's speed
    tom_speed = MATT_SPEED + TOM_EXTRA_SPEED

    # Calculate the number of steps Tom has gone up
    tom_steps = tom_speed * matt_time

    # Display the number of steps Tom has gone up
    result = tom_steps
    return result

print(solution())