def solution():
    """If two trains depart from a station in opposite directions, and one train is traveling 60 miles an hour while the other is traveling half that distance per hour, how far apart are they from each other after 3 hours?"""
    train1_speed = 60
    train2_speed = train1_speed / 2
    time = 3
    distance = (train1_speed + train2_speed) * time
    result = distance
    return result

print(solution())