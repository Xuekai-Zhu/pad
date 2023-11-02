def solution():
    """Mobius is the fastest mule in Italy.  She can run at a top speed of 13 miles per hour when she is without any load to carry, and she can travel at 11 miles per hour as her top speed when she carries a typical load.  If she travels the 143 miles from Florence, Italy to Rome, Italy at top speed while carrying a typical load, then returns to Florence at her usual top speed without carrying a load, how long, in hours, will the trip take if she takes two 30-minute rest stops during each half of the trip?"""
    # Calculate the time it takes Mobius to travel from Florence to Rome
    speed_with_load = 11
    distance = 143
    travel_time = distance/speed_with_load

    # Calculate the time it takes Mobius to travel back from Rome to Florence
    speed_without_load = 13
    distance = 143
    return_time = distance/speed_without_load

    # Calculate total time with rest stops
    rest_stops = 2
    rest_time = 0.5 # in hours
    total_time = travel_time + return_time + (rest_stops * rest_time)

    result = total_time
    return result

print(solution())