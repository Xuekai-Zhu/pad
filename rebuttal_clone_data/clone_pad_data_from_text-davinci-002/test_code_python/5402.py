def solution():
    departure_time = 6
    flight_time_to_chicago = 4
    layover_time = 1
    flight_time_to_miami = flight_time_to_chicago * 3
    total_time = departure_time + flight_time_to_chicago + layover_time + flight_time_to_miami
    result = total_time
    return result

print(solution())