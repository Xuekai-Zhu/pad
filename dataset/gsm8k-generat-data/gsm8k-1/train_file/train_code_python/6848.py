def solution():
    """Mobius is the fastest mule in Italy. She can run at a top speed of 13 miles per hour when she is without any load to carry, and she can travel at 11 miles per hour as her top speed when she carries a typical load. If she travels the 143 miles from Florence, Italy to Rome, Italy at top speed while carrying a typical load, then returns to Florence at her usual top speed without carrying a load, how long, in hours, will the trip take if she takes two 30-minute rest stops during each half of the trip?"""
    distance = 143
    speed_with_load = 11
    speed_without_load = 13
    time_to_rome = distance / speed_with_load
    time_to_florence = distance / speed_without_load
    total_time = (time_to_rome + time_to_florence) + 1  # adding 1 hour for rest stops
    result = total_time
    return result

print(solution())