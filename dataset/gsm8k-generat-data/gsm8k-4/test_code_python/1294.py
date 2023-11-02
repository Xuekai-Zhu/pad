def solution():
    """To get to an island called "Virgo", Tom needs to travel by plane and then by boat. The plane trip is four times longer than the boat trip, and the boat trip takes up to 2 hours. In how many hours is Tom able to get to the "Virgo" island?"""
    # Define the duration of the boat trip
    boat_duration = 2

    # Calculate the duration of the plane trip
    plane_duration = boat_duration * 4

    # Calculate the total duration of the journey
    total_duration = plane_duration + boat_duration

    result = total_duration
    return result

print(solution())