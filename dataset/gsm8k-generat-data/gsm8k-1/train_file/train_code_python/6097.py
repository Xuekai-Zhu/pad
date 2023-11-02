def solution():
    """Matt and Tom both walk up the stairs of the library. Matt goes up the stairs 20 steps per minute. Tom goes up the stairs 5 steps per minute more than Matt. If Matt has reached 220 steps above the entrance, how many steps will Tom have gone up by that time?"""
    matt_speed = 20
    tom_speed = matt_speed + 5
    matt_steps = 220
    time_taken = matt_steps / matt_speed
    tom_steps = tom_speed * time_taken
    result = tom_steps
    return result

print(solution())