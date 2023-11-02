def solution():
    """A plane takes off at 6:00 a.m. and flies for 4 hours from New York City to Chicago. The plane stays at the port in Chicago for 1 hour and then departs for Miami. If the aircraft took three times as many hours to fly to Miami than it took to fly from New York to Chicago, calculate the total time to travel from New York to Miami."""
    # Define the flight times
    flight_time_to_chicago = 4
    port_time = 1
    flight_time_to_miami = 3 * flight_time_to_chicago

    # Calculate the total travel time
    total_time = flight_time_to_chicago + port_time + flight_time_to_miami

    # return the result
    result = total_time
    return result

print(solution())