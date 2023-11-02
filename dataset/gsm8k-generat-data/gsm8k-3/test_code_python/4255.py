def solution():
    """Jeannie hikes the 12 miles to Mount Overlook at a pace of 4 miles per hour, and then returns at a pace of 6 miles per hour. How long did her hike take, in hours?"""
    # Define the distance of the hike
    distance = 12

    # Calculate the time taken to hike to the overlook
    time1 = distance / 4

    # Calculate the time taken to hike back from the overlook
    time2 = distance / 6

    # Calculate the total time of the hike
    total_time = time1 + time2

    # Display the total time
    result = total_time
    return result

print(solution())