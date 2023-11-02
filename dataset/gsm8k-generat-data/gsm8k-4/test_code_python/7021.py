def solution():
    """There is a road stretching 3 miles from the base camp to the chain challenge. Every 20 minutes, a car comes down the road from the base camp towards the chain challenge. How many hours have passed once 30 cars have come down the road?"""
    # Define the distance from base camp to chain challenge
    distance = 3  # miles

    # Define the number of cars
    cars = 30

    # Define the time it takes for a car to travel the distance
    time_per_car = 20 / 60  # hours

    # Calculate the total time
    total_time = cars * time_per_car

    # Return the result in hours
    result = total_time
    return result

print(solution())