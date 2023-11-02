def solution():
    # Calculate the time it took Sue to travel from New York to San Francisco
    time_to_SF = 16 + 24  # 16 hours of waiting time + 24 hours of travel time

    # Calculate the time it took Sue to travel from New Orleans to New York
    time_to_NY = (3/4) * time_to_SF

    # Calculate the total time it took Sue to reach San Francisco from New Orleans
    total_time = time_to_SF + time_to_NY
    result = total_time
    return result

print(solution())