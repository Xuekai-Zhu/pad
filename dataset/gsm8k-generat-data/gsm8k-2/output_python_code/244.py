def solution():
    """A fox can run at the maximum speed of 50 kilometers per hour. Considering the fox would run at a constant speed, what distance would he make during 120 minutes?"""
    fox_speed = 50  # km/hour
    time = 120  # minutes
    distance = (fox_speed / 60) * (time / 60)
    result = distance
    return result

print(solution())