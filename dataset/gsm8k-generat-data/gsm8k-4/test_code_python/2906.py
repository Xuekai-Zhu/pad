def solution():
    """There are 20 bicycles, 10 cars and 5 motorcycles in the garage at Connor's house. How many wheels are there in the garage?"""
    # Define the number of wheels for each type of vehicle
    BIKE_WHEELS = 2
    CAR_WHEELS = 4
    MOTORCYCLE_WHEELS = 2

    # Calculate the total number of wheels in the garage
    total_wheels = (20 * BIKE_WHEELS) + (10 * CAR_WHEELS) + (5 * MOTORCYCLE_WHEELS)

    # Return the result
    result = total_wheels
    return result

print(solution())