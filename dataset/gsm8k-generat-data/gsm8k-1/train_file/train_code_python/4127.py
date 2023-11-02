def solution():
    """Sonia and Joss are moving to their new house at the lake. They have too much stuff in their previous house and decide to make multiple trips to move it all to the new house. They spend 15 minutes filling the car with their stuff and spend 30 minutes driving from the previous house to the new house. Fortunately, they did not waste any time unloading their stuff into the new house. In total they make 6 trips to complete the move. How many hours did they spend moving?"""
    time_per_trip = 45 # 15 minutes filling the car + 30 minutes driving
    total_trips = 6
    total_time_in_minutes = time_per_trip * total_trips
    total_time_in_hours = total_time_in_minutes / 60
    result = total_time_in_hours
    return result

print(solution())