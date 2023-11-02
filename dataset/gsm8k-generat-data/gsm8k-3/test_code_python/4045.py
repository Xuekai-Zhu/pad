def solution():
    """Laura took six trips to park. On each trip, she spent 2 hours at the park and an additinal 30 minutes walking to and from the park. What percentage of the total time she took for her trips to the park did Laura spend in the park?"""
    # Define total time spent for each trip
    trip_time = 2.5  # 2 hours at the park + 30 minutes of walking

    # Calculate total time spent for all trips
    total_time = trip_time * 6

    # Calculate total time spent in the park
    park_time = 2 * 6  # 2 hours at the park for each of the 6 trips

    # Calculate percentage of total time spent in the park
    percentage = (park_time/total_time) * 100

    # Display percentage of total time spent in the park
    result = percentage
    return result

print(solution())