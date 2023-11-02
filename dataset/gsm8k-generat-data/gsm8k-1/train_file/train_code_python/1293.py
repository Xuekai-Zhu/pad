def solution():
    """To get to an island called "Virgo", Tom needs to travel by plane and then by boat. The plane trip is four times longer than the boat trip, and the boat trip takes up to 2 hours. In how many hours is Tom able to get to the "Virgo" island?"""
    boat_trip = 2
    plane_trip = boat_trip * 4
    total_trip_time = boat_trip + plane_trip
    result = total_trip_time
    return result

print(solution())