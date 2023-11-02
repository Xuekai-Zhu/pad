def solution():
    # Calculate the time taken to travel from New York to San Francisco
    ny_sf_time = 24

    # Calculate the time taken to travel from New Orleans to New York
    no_ny_time = ny_sf_time * 4 / 3

    # Calculate the total time taken to reach San Francisco from New Orleans
    total_time = no_ny_time + ny_sf_time + 16

    result = total_time
    return result

print(solution())