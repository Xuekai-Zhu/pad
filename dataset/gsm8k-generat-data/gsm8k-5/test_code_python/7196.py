def solution():
    flight_time = 11 * 60 + 20  # Convert flight time to minutes
    activities_time = 2 * 60 + 4 * 60 + 30 + 40 + 1 * 60 + 10  # Convert activities time to minutes
    nap_time = (flight_time - activities_time) / 60  # Convert remaining time to hours

    result = nap_time
    return result

print(solution())