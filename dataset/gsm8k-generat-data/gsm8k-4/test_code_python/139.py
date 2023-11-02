def solution():
    """Janice's office is on the third floor, and she has to walk up 3 flights of stairs to get to her office. In a single day, she goes up the three flights of stairs 5 times, down the the three flights of stairs 3 times, and uses the elevator the remainder of the time. How many flights of stairs does Janice walk (up and down) in a single day?"""
    # Define the number of flights of stairs per floor
    FLIGHTS_PER_FLOOR = 3

    # Calculate the total number of flights of stairs Janice walks up each day
    up_flights = 5 * FLIGHTS_PER_FLOOR

    # Calculate the total number of flights of stairs Janice walks down each day
    down_flights = 3 * FLIGHTS_PER_FLOOR

    # Calculate the total number of flights of stairs Janice walks (up and down) each day
    total_flights = up_flights + down_flights

    # return the result
    result = total_flights
    return result

print(solution())