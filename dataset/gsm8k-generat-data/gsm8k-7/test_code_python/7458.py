def solution():
    track_distance = 0.25  # miles
    polly_laps = 12
    polly_time = 0.5  # hours

    polly_speed = (polly_laps * track_distance) / polly_time

    gerald_speed = polly_speed / 2  # since Gerald's car moves at half the speed of Polly's

    # Convert speed from miles per minute to miles per hour
    gerald_speed = gerald_speed * 60

    result = gerald_speed
    return result

print(solution())