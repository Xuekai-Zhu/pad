def solution():
    """Janice's office is on the third floor, and she has to walk up 3 flights of stairs to get to her office. In a single day, she goes up the three flights of stairs 5 times, down the the three flights of stairs 3 times, and uses the elevator the remainder of the time. How many flights of stairs does Janice walk (up and down) in a single day?"""
    # Define the number of flights of stairs Janice has to walk up and down once
    stairs_per_trip = 6

    # Define the number of trips Janice takes up the stairs and down the stairs each day
    trips_up = 5
    trips_down = 3

    # Calculate the total number of flights of stairs Janice walks up and down each day
    total_stairs = (trips_up + trips_down) * stairs_per_trip

    # Return the result
    result = total_stairs
    return result

print(solution())