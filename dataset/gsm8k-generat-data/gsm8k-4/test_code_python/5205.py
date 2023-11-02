def solution():
    """A marathon is 26 miles. He can run the first 10 miles in 1 hour. For the remaining miles he runs at 80% that pace. How long does the race take?"""
    # Define the total distance and the distance covered in the first hour
    total_distance = 26
    distance_first_hour = 10

    # Calculate the remaining distance and the time taken to cover it at 80% of the first hour's pace
    remaining_distance = total_distance - distance_first_hour
    time_remaining_distance = remaining_distance / (0.8 * distance_first_hour)

    # Calculate the total time taken to complete the marathon
    total_time = 1 + time_remaining_distance

    # Return the result in hours and minutes
    result = f"{int(total_time)} hours {int((total_time - int(total_time)) * 60)} minutes"
    return result

print(solution())