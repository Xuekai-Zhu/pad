def solution():
    """Peter and Andrew like to run in the morning.  Peter runs 3 miles more than Andrew's 2 miles.  After 5 days, how many miles have they both run?"""
    # Define Andrew's daily distance
    andrew_distance = 2

    # Define Peter's daily distance
    peter_distance = andrew_distance + 3

    # Calculate the total distance run by both of them after 5 days
    total_distance = 5 * (andrew_distance + peter_distance)

    # Display the total distance run by both of them after 5 days
    result = total_distance
    return result

print(solution())