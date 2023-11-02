def solution():
    """Some friends went hiking for 3.5 hours. They traveled 21 kilometers in that time. Birgit was 4 minutes/km faster than the average time. If Birgit kept the same pace, how many minutes would it take her to go 8 kilometers?"""
    # Define the total time taken and the distance traveled
    total_time = 3.5
    distance = 21

    # Calculate the average speed and the time taken per kilometer
    speed = distance / total_time
    time_per_km = 60 / speed

    # Calculate Birgit's time per kilometer
    birgit_time_per_km = time_per_km - 4

    # Calculate Birgit's time to travel 8 kilometers
    birgit_time_8km = birgit_time_per_km * 8

    # Return the result in minutes
    result = birgit_time_8km
    return result

print(solution())