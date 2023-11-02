def solution():
    # Calculate the time it will take on the first route if all lights are red
    red_lights_time = 10 + 3 * 3  # each red light adds 3 minutes
    extra_time = red_lights_time - 10 # Calculate the extra time if all lights are red
    result = extra_time
    return result

print(solution())