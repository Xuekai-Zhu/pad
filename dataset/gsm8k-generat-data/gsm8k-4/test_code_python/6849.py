def solution():
    """Mobius is the fastest mule in Italy.  She can run at a top speed of 13 miles per hour when she is without any load to carry,
    and she can travel at 11 miles per hour as her top speed when she carries a typical load.  If she travels the 143 miles from Florence, 
    Italy to Rome, Italy at top speed while carrying a typical load, then returns to Florence at her usual top speed without carrying 
    a load, how long, in hours, will the trip take if she takes two 30-minute rest stops during each half of the trip?"""
    # Define the distance from Florence to Rome
    distance = 143

    # Define the top speeds with and without the load
    top_speed_with_load = 11
    top_speed_without_load = 13

    # Calculate the time taken to travel to Rome with rest stops
    time_to_rome = (distance / top_speed_with_load) + 1

    # Calculate the time taken to travel back to Florence without a load with rest stops
    time_to_florence = (distance / top_speed_without_load) + 1

    # Calculate the total time taken with rest stops
    total_time = (time_to_rome + time_to_florence) + 1

    # return the result
    result = total_time
    return result

print(solution())