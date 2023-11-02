def solution():
    """Jerome is taking a 150-mile bicycle trip. He wants to ride 12 miles for 12 days. How long will he ride on the 13th day to finish his goal?"""
    # Define the total distance of the trip
    total_distance = 150

    # Define the distance he rides per day for 12 days
    daily_distance = 12

    # Calculate the distance he has already ridden
    ridden_distance = daily_distance * 12

    # Calculate the remaining distance
    remaining_distance = total_distance - ridden_distance

    # Calculate the distance he needs to ride on the 13th day to finish his goal
    distance_13th_day = remaining_distance

    # return the result
    result = distance_13th_day
    return result

print(solution())