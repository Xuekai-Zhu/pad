def solution():
    # Calculate the total time spent reading
    total_time = 3 * (3/4)  # he spent only three-quarters of his planned time reading

    # Calculate the number of pages read
    pages_per_hour = 4  # he can read 4 pages per hour (since he reads a page every 15 minutes)
    total_pages = pages_per_hour * total_time

    result = total_pages
    return result

print(solution())