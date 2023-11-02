def solution():
    """Polly and Gerald went for a fun afternoon riding mini race cars at the munchkin track, which is a one-quarter mile circular track. Polly managed to circle the track 12 times in one half hour, but Gerald's car was malfunctioning, and he only moved at an average speed half of what Polly did. What speed did Gerald's car average, in miles per hour?"""
    track_length = 0.25
    polly_laps = 12
    polly_time = 0.5
    polly_speed = polly_laps * track_length / polly_time
    gerald_speed = polly_speed / 2
    mph_conversion = 60 / 1.6
    result = gerald_speed * mph_conversion
    return result

print(solution())