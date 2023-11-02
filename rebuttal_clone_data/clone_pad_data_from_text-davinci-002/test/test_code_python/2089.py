def solution():
    initial_elevation = 400
    elevation_change = -10
    minutes = 5
    total_change = elevation_change * minutes
    final_elevation = initial_elevation + total_change
    result = final_elevation
    return result

print(solution())