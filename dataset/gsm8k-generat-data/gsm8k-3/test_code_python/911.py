def solution():
    """It took an alligator named Paul 4 hours to walk from his home at the River Nile to the Nile Delta.
    On the return journey, Paul traveled with six other alligators, the journey taking 2 more hours than Paul
    took to walk to the Nile Delta, to reach their home at the River Nile. What's the combined time the alligators walked?"""
    # Let's assume the distance between the River Nile and the Nile Delta is 'd'
    # Let's also assume that Paul's walking speed is 's'

    # Speed = Distance/Time, therefore the time taken by Paul to walk to the Nile Delta is:
    time_to_delta = 4  # hours

    # On the return journey, Paul traveled with six other alligators, i.e., 7 alligators in total,
    # so the speed of the alligators would be 7s.
    # The journey took 2 more hours than Paul took to walk to the Nile Delta, so the time taken would be:
    time_to_home = time_to_delta + 2  # hours

    # The total distance traveled by Paul and the other alligators is 2d:
    total_distance = 2*d

    # Total time taken by Paul and the other alligators:
    total_time = time_to_delta + time_to_home

    # Distance = Speed*Time, therefore the walking speed 's' of Paul is:
    s = d/time_to_delta

    # The distance 'd' can now be calculated as:
    d = s*time_to_delta

    # The combined time the alligators walked is:
    result = total_time
    return result

print(solution())