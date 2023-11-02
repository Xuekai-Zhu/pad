def solution():
    """The journey from Abel's house to Alice's house is 35 miles and is divided into 5 equal portions. Abel is driving at a speed of 40 miles per hour. After traveling for 0.7 hours, how many portions of the journey has he covered?"""
    journey_distance = 35
    portion_distance = journey_distance / 5
    speed = 40
    time = 0.7
    distance_traveled = speed * time
    portions_covered = distance_traveled / portion_distance
    result = portions_covered
    return result

print(solution())