def solution():
    """Jerome is taking a 150-mile bicycle trip. He wants to ride 12 miles for 12 days. How long will he ride on the 13th day to finish his goal?"""
    # Define the total distance and the number of days
    total_distance = 150
    num_days = 12

    # Calculate the distance already covered
    distance_covered = num_days * 12

    # Calculate the remaining distance
    remaining_distance = total_distance - distance_covered

    # Calculate the distance to be covered on the 13th day
    day_13_distance = remaining_distance % 12

    # Return the result
    result = day_13_distance
    return result

print(solution())