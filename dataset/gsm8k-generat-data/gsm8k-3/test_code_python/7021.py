def solution():
    """There is a road stretching 3 miles from the base camp to the chain challenge. Every 20 minutes, a car comes down the road from the base camp towards the chain challenge. How many hours have passed once 30 cars have come down the road?"""
    # Define the distance of the road and the time it takes for one car to travel the distance
    distance = 3
    time_per_car = 20 / 60  # convert 20 minutes to hours

    # Calculate the total time it takes for 30 cars to come down the road
    total_time = time_per_car * 30

    # Display the total time in hours
    result = total_time
    return result

print(solution())