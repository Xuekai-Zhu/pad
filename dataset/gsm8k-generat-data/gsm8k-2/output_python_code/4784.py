def solution():
    """Every day, Lou works out by running three miles on a circular track that is one-quarter of a mile long. His wife, Rosie, also runs on the same track at the same time as her husband, but she runs at twice the speed of her husband. During their workout, how many times does Rosie circle the track?"""
    lou_distance = 3
    track_length = 0.25
    lou_laps = lou_distance / track_length
    rosie_laps = lou_laps * 2
    result = rosie_laps
    return result

print(solution())