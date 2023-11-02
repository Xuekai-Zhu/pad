def solution():
    """A marathon is 26 miles.  He can run the first 10 miles in 1 hour.  For the remaining miles he runs at 80% that pace.  How long does the race take?"""
    # Define the distance and initial pace
    distance = 26
    initial_pace = 10

    # Calculate the time it takes to run the first 10 miles
    time1 = 1

    # Calculate the remaining distance and new pace
    remaining_distance = distance - initial_pace
    new_pace = 0.8

    # Calculate the time it takes to run the remaining distance
    time2 = remaining_distance * new_pace

    # Calculate the total time for the race
    total_time = time1 + time2

    # Display the total time
    result = total_time
    return result

print(solution())