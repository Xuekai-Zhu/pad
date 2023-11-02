def solution():
    """Calculate the number of hours Chance's flight took from New York to Cape Town"""
    initial_arrival_time = 18  # This is the time in hours from departure to arrival in New York
    time_difference = 6  # This is the difference in hours between London time and New York time
    total_time = (10 - time_difference + 24) % 24 - initial_arrival_time  # This calculates the total time in hours from New York to Cape Town
    result = total_time
    return result

print(solution())