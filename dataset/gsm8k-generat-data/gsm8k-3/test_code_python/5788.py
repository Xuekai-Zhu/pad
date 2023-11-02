def solution():
    """Some friends went hiking for 3.5 hours. They traveled 21 kilometers in that time. Birgit was 4 minutes/km faster than the average time. If Birgit kept the same pace, how many minutes would it take her to go 8 kilometers?"""
    # Calculate the average speed in km/h
    average_speed = 21 / 3.5

    # Calculate the average time in minutes/km
    average_time = 60 / average_speed

    # Calculate Birgit's time in minutes/km
    birgit_time = average_time - 4

    # Calculate the time it would take Birgit to go 8 km
    time_to_8km = birgit_time * 8

    # Display the time in minutes
    result = time_to_8km
    return result

print(solution())