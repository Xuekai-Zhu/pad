def solution():
    # Calculate the average speed in km/h
    speed = 21 / 3.5

    # Convert the speed to minutes/km
    average_time = 60 / speed

    # Calculate Birgit's time for 8 km
    birgit_time = average_time - 4

    # Convert Birgit's time to minutes
    birgit_time_in_minutes = birgit_time * 8

    result = birgit_time_in_minutes
    return result

print(solution())