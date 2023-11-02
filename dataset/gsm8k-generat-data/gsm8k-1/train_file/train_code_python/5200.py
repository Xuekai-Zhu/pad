def solution():
    """Three train stations are 2 hours apart from one another. Kira travels from the first station to the third, taking a 30 minutes break at the second station. What's the total time, in minutes, that Kira takes to travel between the first and third station?"""
    time_between_stations = 2 * 60
    break_time = 30
    total_travel_time = time_between_stations + break_time
    result = total_travel_time
    return result

print(solution())