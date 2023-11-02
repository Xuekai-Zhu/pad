def solution():
    # Calculate the average number of shots per minute
    shots_per_minute = 60 / 15

    # Calculate the average number of seconds per shot
    seconds_per_shot = 5

    # Calculate the average number of seconds per minute that Jason shoots flames
    seconds_per_minute = shots_per_minute * seconds_per_shot

    result = seconds_per_minute
    return result

print(solution())