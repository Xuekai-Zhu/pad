def solution():
    flights_per_trip = 3  # Janice walks up and down 3 flights of stairs per trip
    trips_up = 5  # Janice goes up the three flights of stairs 5 times
    trips_down = 3  # Janice goes down the three flights of stairs 3 times
    total_trips = trips_up + trips_down  # Janice makes a total of 8 trips
    total_flights = total_trips * flights_per_trip

    result = total_flights
    return result

print(solution())