def solution():
    """Polly and Gerald went for a fun afternoon riding mini race cars at the munchkin track, which is a one-quarter mile circular track. Polly managed to circle the track 12 times in one half hour, but Gerald's car was malfunctioning, and he only moved at an average speed half of what Polly did. What speed did Gerald's car average, in miles per hour?"""
    distance_per_lap = 0.25
    laps_polly = 12
    time_half_hour = 0.5
    speed_polly = (distance_per_lap * laps_polly) / time_half_hour
    speed_gerald = speed_polly / 2
    result = speed_gerald * 2  # convert from half hour to hour
    return result

print(solution())