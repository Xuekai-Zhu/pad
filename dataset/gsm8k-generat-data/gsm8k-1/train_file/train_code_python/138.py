def solution():
    """Janice's office is on the third floor, and she has to walk up 3 flights of stairs to get to her office. In a single day, she goes up the three flights of stairs 5 times, down the the three flights of stairs 3 times, and uses the elevator the remainder of the time. How many flights of stairs does Janice walk (up and down) in a single day?"""
    floors_per_flight = 3
    up_flights_per_day = 5
    down_flights_per_day = 3
    total_flights_per_day = (up_flights_per_day + down_flights_per_day) * floors_per_flight
    result = total_flights_per_day
    return result

print(solution())