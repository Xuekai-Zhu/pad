def solution():
    """Matt and Tom both walk up the stairs of the library. Matt goes up the stairs 20 steps per minute. Tom goes up the stairs 5 steps per minute more than Matt. If Matt has reached 220 steps above the entrance, how many steps will Tom have gone up by that time?"""
    # Define Matt's speed and the number of steps he has climbed
    matt_speed = 20
    matt_steps = 220

    # Calculate Tom's speed and the number of steps he has climbed
    tom_speed = matt_speed + 5
    tom_steps = ((matt_steps * tom_speed) / matt_speed)

    result = int(tom_steps)
    return result

print(solution())