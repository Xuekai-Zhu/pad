def solution():
    """Janice's office is on the third floor, and she has to walk up 3 flights of stairs to get to her office. In a single day, she goes up the three flights of stairs 5 times, down the the three flights of stairs 3 times, and uses the elevator the remainder of the time. How many flights of stairs does Janice walk (up and down) in a single day?"""
    flights_per_trip = 6
    trips_up = 5
    trips_down = 3
    total_trips = trips_up + trips_down
    total_flights = total_trips * flights_per_trip
    result = total_flights
    return result

print(solution())