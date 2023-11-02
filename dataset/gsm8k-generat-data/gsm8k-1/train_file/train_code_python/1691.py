def solution():
    """Sue is traveling from New York to San Francisco, 16 hours later after landing in New York from New Orleans. If the journey from New Orleans to New York took 3/4 times as much time as she takes to travel from New York to San Francisco, and she lands in San Francisco 24 hours later after departing from New York, calculate the total time she took to reach San Francisco from New Orleans?"""
    time_to_SF_from_NY = 24
    time_to_NY_from_NO = (3/4) * time_to_SF_from_NY
    total_time = time_to_SF_from_NY + time_to_NY_from_NO + 16
    result = total_time
    return result

print(solution())