def solution():
    """If Amanda can run the length of a football field 2000 meters in length in 2 hours, how long would it take her to run the length of a 10000-meter track at the same speed?"""
    football_field_distance = 2000
    football_field_time = 2 * 60  # convert to minutes
    speed = football_field_distance / football_field_time
    track_distance = 10000
    track_time = track_distance / speed
    result = track_time
    return result

print(solution())