def solution():
    """The bus driver drives an average of 2 hours each day, 5 days a week. From Monday to Wednesday he drove at an average speed of 12 kilometers per hour, and from Thursday to Friday at an average speed of 9 kilometers per hour. How many kilometers did the driver travel during these 5 days?"""
    # Define the average driving time per day and the number of days driven
    driving_time = 2
    driving_days = 5

    # Define the average speed for each period
    speed_1 = 12
    speed_2 = 9

    # Calculate the total distance driven from Monday to Wednesday
    distance_1 = speed_1 * driving_time * 3

    # Calculate the total distance driven from Thursday to Friday
    distance_2 = speed_2 * driving_time * 2

    # Calculate the total distance driven
    total_distance = distance_1 + distance_2

    # return the result
    result = total_distance
    return result

print(solution())