def solution():
    """Mira jogs every morning. She jogs 5 miles per hour. If she jogs for 2 hours every morning, how many miles can she jog for five days?"""
    # Define Mira's jogging speed and time
    speed = 5 # mph
    time = 2 # hours/day

    # Calculate the distance Mira can jog in one day
    distance = speed * time

    # Calculate the total distance Mira can jog in five days
    total_distance = distance * 5

    result = total_distance
    return result

print(solution())