def solution():
    """Nina loves to travel. She tries to travel at least 400 kilometers in one month outside of her home country. Every second month she does twice that distance. If she were able to keep up with her resolution, how many kilometers would she travel during 2 years?"""
    # Define the minimum distance Nina travels every month and the factor for the second month
    MIN_DISTANCE = 400
    FACTOR = 2

    # Initialize the total distance traveled and the factor counter
    total_distance = 0
    factor_counter = 0

    # Calculate the distance traveled for each month in 2 years (24 months)
    for i in range(24):
        if factor_counter == 1:
            # For the second month, double the minimum distance
            distance = MIN_DISTANCE * FACTOR
            factor_counter = 0
        else:
            # For other months, use the minimum distance
            distance = MIN_DISTANCE
            factor_counter += 1
        total_distance += distance

    # return the result
    result = total_distance
    return result

print(solution())