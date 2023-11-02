def solution():
    """Nina loves to travel. She tries to travel at least 400 kilometers in one month outside of her home country. Every second month she does twice that distance. If she were able to keep up with her resolution, how many kilometers would she travel during 2 years?"""
    # Define the minimum distance Nina travels in a month
    MIN_DISTANCE = 400

    # Calculate the total distance Nina travels in one year
    total_distance_per_year = 0
    for i in range(0, 24):
        if i % 2 == 0:
            total_distance_per_year += MIN_DISTANCE
        else:
            total_distance_per_year += MIN_DISTANCE * 2

    # Calculate the total distance Nina travels in two years
    total_distance = total_distance_per_year * 2

    # Display the total distance Nina travels
    result = total_distance
    return result

print(solution())