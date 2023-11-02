def solution():
    meso_rate = 15 / 5  # Meso types 3 pages per minute
    tyler_rate = 15 / 3  # Tyler types 5 pages per minute
    total_rate = meso_rate + tyler_rate  # Combined rate is 8 pages per minute
    total_pages = 40
    total_time = total_pages / total_rate  # Time in minutes to type 40 pages
    result = total_time
    return result

print(solution())