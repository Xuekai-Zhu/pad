def solution():
    """There is a road stretching 3 miles from the base camp to the chain challenge. Every 20 minutes, a car comes down the road from the base camp towards the chain challenge. How many hours have passed once 30 cars have come down the road?"""
    distance = 3  # miles
    time_per_car = 20  # minutes
    cars_to_reach = 30
    total_time = (cars_to_reach * time_per_car) / 60  # convert minutes to hours
    result = total_time
    return result

print(solution())