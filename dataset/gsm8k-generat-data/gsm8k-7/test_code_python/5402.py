def solution():
    takeoff_time = 6  # 6:00 a.m.
    fly_time_to_chicago = 4  # 4 hours
    port_time = 1  # 1 hour
    fly_time_to_miami = 3 * fly_time_to_chicago  # 3 times the fly_time_to_chicago

    # Calculate the landing time in Chicago
    landing_time_chicago = takeoff_time + fly_time_to_chicago

    # Calculate the departure time from Chicago
    departure_time_chicago = landing_time_chicago + port_time

    # Calculate the landing time in Miami
    landing_time_miami = departure_time_chicago + fly_time_to_miami

    # Calculate the total travel time from New York to Miami
    total_travel_time = landing_time_miami - takeoff_time
    result = total_travel_time
    return result

print(solution())