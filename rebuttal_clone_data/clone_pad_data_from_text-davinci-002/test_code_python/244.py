def solution():
    """A fox can run at the maximum speed of 50 kilometers per hour. Considering the fox would run at a constant speed, what distance would he make during 120 minutes?"""
    max_speed = 50
    minutes = 120
    hours = minutes / 60
    distance = max_speed * hours
    result = distance
    return result

print(solution())