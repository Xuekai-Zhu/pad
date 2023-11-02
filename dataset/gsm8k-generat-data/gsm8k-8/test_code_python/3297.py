def solution():
    # Define the distance and number of days for the first period
    dist1 = 30
    days1 = 183

    # Calculate the total distance for the first period
    total_dist1 = dist1 * days1

    # Define the distance and number of days for the second period
    dist2 = 35
    days2 = 182

    # Calculate the total distance for the second period
    total_dist2 = dist2 * days2

    # Calculate the total distance for the year
    total_dist = total_dist1 + total_dist2
    result = total_dist
    return result

print(solution())