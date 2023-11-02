def solution():
    """Sue is traveling from New York to San Francisco, 16 hours later after landing in New York from New Orleans. If the journey from New Orleans to New York took 3/4 times as much time as she takes to travel from New York to San Francisco, and she lands in San Francisco 24 hours later after departing from New York, calculate the total time she took to reach San Francisco from New Orleans?"""
    # Calculate the time Sue spent traveling from New Orleans to New York
    time_NO_to_NY = (3/4) * (24 + 16)

    # Calculate the total time Sue spent traveling from New Orleans to San Francisco
    total_time = time_NO_to_NY + 16 + 24

    # return the result
    result = total_time
    return result

print(solution())