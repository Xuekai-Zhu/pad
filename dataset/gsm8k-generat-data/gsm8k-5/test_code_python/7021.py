def solution():
    distance = 3  # The road is 3 miles long
    cars_per_20_minutes = 1  # One car comes down the road every 20 minutes
    cars_needed = 30  # We need 30 cars to come down the road
    time_per_car = 1 / (cars_per_20_minutes / 3)  # Each car takes 3/20 hours to travel the distance
    total_time = time_per_car * cars_needed  # Total time it takes for 30 cars to come down the road
    
    # Convert total time to hours
    hours = total_time / 60
    result = hours
    return result

print(solution())