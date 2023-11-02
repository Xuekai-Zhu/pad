def solution():
    """A plane takes off at 6:00 a.m. and flies for 4 hours from New York City to Chicago. The plane stays at the port in Chicago for 1 hour and then departs for Miami. If the aircraft took three times as many hours to fly to Miami than it took to fly from New York to Chicago, calculate the total time to travel from New York to Miami."""
    ny_to_chicago_time = 4
    chicago_to_miami_time = ny_to_chicago_time * 3
    total_travel_time = ny_to_chicago_time + 1 + chicago_to_miami_time
    result = total_travel_time
    return result

print(solution())