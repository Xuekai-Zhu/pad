def solution():
    # Calcuate Joy's reading speed in pages per minute
    pages_per_min = 8/20

    # Calculate the total time it will take Joy to read 120 pages
    total_time_in_min = 120/pages_per_min

    # Convert the total time to hours
    total_time_in_hours = total_time_in_min/60
    
    result = total_time_in_hours
    return result

print(solution())