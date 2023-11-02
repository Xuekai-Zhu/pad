def solution():
    """Sue is traveling from New York to San Francisco, 16 hours later after landing in New York from New Orleans. If the journey from New Orleans to New York took 3/4 times as much time as she takes to travel from New York to San Francisco, and she lands in San Francisco 24 hours later after departing from New York, calculate the total time she took to reach San Francisco from New Orleans?"""
    
    # Calculate the time taken to travel from New York to San Francisco
    ny_sf_time = 24
    
    # Calculate the time taken to travel from New Orleans to New York
    no_ny_time = ny_sf_time * (4/3)
    
    # Calculate the total time taken
    total_time = no_ny_time + 16 + ny_sf_time
    
    # Display the total time taken
    result = total_time
    return result

print(solution())