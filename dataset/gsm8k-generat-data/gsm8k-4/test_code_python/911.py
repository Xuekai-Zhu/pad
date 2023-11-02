def solution():
    """It took an alligator named Paul 4 hours to walk from his home at the River Nile to the Nile Delta. On the return journey, Paul traveled with six other alligators, the journey taking 2 more hours than Paul took to walk to the Nile Delta, to reach their home at the River Nile. What's the combined time the alligators walked?"""
    # Define the time Paul spent walking to the Nile Delta
    paul_time_to_delta = 4

    # Calculate Paul's return journey time
    paul_return_time = paul_time_to_delta + 2

    # Find the total time it took the group of alligators to make the return journey
    group_return_time = paul_return_time * (1/7)

    # Find the combined time the alligators walked
    combined_time = paul_time_to_delta + group_return_time

    result = combined_time
    return result

print(solution())