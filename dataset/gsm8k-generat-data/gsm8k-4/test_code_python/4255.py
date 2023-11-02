def solution():
    """Jeannie hikes the 12 miles to Mount Overlook at a pace of 4 miles per hour, and then returns at a pace of 6 miles per hour. How long did her hike take, in hours?"""
    # Define the distance to be hiked
    distance = 12

    # Calculate the time taken to hike to the top
    time_to_top = distance / 4

    # Calculate the time taken to hike down
    time_to_bottom = distance / 6

    # Calculate the total time taken for the hike
    total_time = time_to_top + time_to_bottom

    # Return the result
    result = total_time
    return result

print(solution())