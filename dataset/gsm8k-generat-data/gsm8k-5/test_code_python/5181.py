def solution():
    distance_jogged = 15 * 0.5  # Jenny jogs for 0.5 hours at 15 miles per hour
    distance_remaining = 15 - distance_jogged  # Distance remaining to school
    time_to_reach_school = distance_remaining / 15  # Time taken to reach school
    time_to_catch_jenny = distance_jogged / (45 - 15)  # Time taken to catch up with Jenny
    total_time = time_to_reach_school + time_to_catch_jenny  # Total time taken

    # Convert total time to minutes
    total_time_minutes = total_time * 60
    result = total_time_minutes
    return result

print(solution())