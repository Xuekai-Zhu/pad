def solution():
    """Sonia and Joss are moving to their new house at the lake. They have too much stuff in their previous house and decide to make multiple trips to move it all to the new house. They spend 15 minutes filling the car with their stuff and spend 30 minutes driving from the previous house to the new house. Fortunately, they did not waste any time unloading their stuff into the new house. In total they make 6 trips to complete the move. How many hours did they spend moving?"""
    fill_time = 15
    drive_time = 30
    total_trips = 6
    one_way_time = fill_time + drive_time
    round_trip_time = one_way_time * 2
    total_time = round_trip_time * total_trips
    total_hours = total_time / 60
    result = total_hours
    return result

print(solution())