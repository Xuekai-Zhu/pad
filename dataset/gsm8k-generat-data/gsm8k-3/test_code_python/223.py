def solution():
    """Mira jogs every morning. She jogs 5 miles per hour. If she jogs for 2 hours every morning, how many miles can she jog for five days?"""
    # Define the number of hours Mira jogs each day
    hours_per_day = 2

    # Define Mira's jogging speed in miles per hour
    speed = 5

    # Calculate the distance Mira can jog in one day
    distance_per_day = speed * hours_per_day

    # Calculate the total distance Mira can jog in five days
    total_distance = distance_per_day * 5

    # Display the total distance Mira can jog in five days
    result = total_distance
    return result

print(solution())