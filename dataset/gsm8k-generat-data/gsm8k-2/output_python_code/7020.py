def solution():
    """There is a road stretching 3 miles from the base camp to the chain challenge. Every 20 minutes, a car comes down the road from the base camp towards the chain challenge. How many hours have passed once 30 cars have come down the road?"""
    time_per_car = 20 / 60  # convert minutes to hours
    total_cars = 30
    total_time = time_per_car * total_cars
    result = total_time
    return result

print(solution())