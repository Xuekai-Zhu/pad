def solution():
    """To get to an island called "Virgo", Tom needs to travel by plane and then by boat. The plane trip is four times longer than the boat trip, and the boat trip takes up to 2 hours. In how many hours is Tom able to get to the "Virgo" island?"""
    # Define the time for the boat trip
    boat_time = 2

    # Define the ratio of the plane trip to the boat trip
    plane_ratio = 4

    # Calculate the time for the plane trip
    plane_time = boat_time * plane_ratio

    # Calculate the total time for the trip
    total_time = boat_time + plane_time

    # Display the total time for the trip
    result = total_time
    return result

print(solution())