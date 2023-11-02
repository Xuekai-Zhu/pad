def solution():
    """Laura took six trips to park. On each trip, she spent 2 hours at the park and an additinal 30 minutes walking to and from the park. What percentage of the total time she took for her trips to the park did Laura spend in the park?"""
    # Define the total number of trips and the time per trip
    total_trips = 6
    trip_time = 2.5

    # Calculate the total time Laura spent on all trips
    total_time = total_trips * trip_time

    # Calculate the total time Laura spent in the park
    park_time = total_trips * 2

    # Calculate the percentage of time spent in the park
    park_percentage = (park_time / total_time) * 100

    # return the result
    result = park_percentage
    return result

print(solution())