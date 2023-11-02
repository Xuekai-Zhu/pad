def solution():
    """A plane takes off at 6:00 a.m. and flies for 4 hours from New York City to Chicago. The plane stays at the port in Chicago for 1 hour and then departs for Miami. If the aircraft took three times as many hours to fly to Miami than it took to fly from New York to Chicago, calculate the total time to travel from New York to Miami."""
    # Define the duration of the flight from New York to Chicago
    ny_to_chicago_duration = 4

    # Define the duration of the layover in Chicago
    layover_duration = 1

    # Calculate the duration of the flight from Chicago to Miami
    chicago_to_miami_duration = ny_to_chicago_duration * 3

    # Calculate the total travel time
    total_time = ny_to_chicago_duration + layover_duration + chicago_to_miami_duration

    # Display the total travel time
    result = total_time
    return result

print(solution())