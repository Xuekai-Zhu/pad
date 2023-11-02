def solution():
    """Janice's office is on the third floor, and she has to walk up 3 flights of stairs to get to her office. In a single day, she goes up the three flights of stairs 5 times, down the the three flights of stairs 3 times, and uses the elevator the remainder of the time. How many flights of stairs does Janice walk (up and down) in a single day?"""
    stairs_to_office = 3
    trips_up_stairs = 5
    trips_down_stairs = 3
    stairs_per_trip = 2
    total_stairs = (trips_up_stairs * stairs_to_office *stairs_per_trip) + (trips_down_stairs * stairs_to_office * stairs_per_trip)
    result = total_stairs
    
    return result

print(solution())