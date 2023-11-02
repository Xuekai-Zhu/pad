def solution():
    """To get to an island called "Virgo", Tom needs to travel by plane and then by boat. The plane trip is four times longer than the boat trip, and the boat trip takes up to 2 hours. In how many hours is Tom able to get to the "Virgo" island?"""
    boat_time = 2
    plane_time = 4 * boat_time
    total_travel_time = boat_time + plane_time
    result = total_travel_time
    return result

print(solution())