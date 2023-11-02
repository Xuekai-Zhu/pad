def solution():
    fire_rate = 1/15 # rate of firing weapon in seconds
    flame_duration = 5 # duration of flame in seconds

    # Calculate the rate of firing flames
    flame_rate = fire_rate * (flame_duration / 60) # convert flame duration to minutes

    result = flame_rate * 60 # convert back to seconds per minute
    return result

print(solution())