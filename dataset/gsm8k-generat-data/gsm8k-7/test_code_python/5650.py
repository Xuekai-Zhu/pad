def solution():
    dustin_rate = 75 / 60  # pages per minute
    sam_rate = 24 / 60  # pages per minute
    time_in_minutes = 40

    # Calculate total pages read by Dustin in 40 minutes
    dustin_pages_read = dustin_rate * time_in_minutes

    # Calculate total pages read by Sam in 40 minutes
    sam_pages_read = sam_rate * time_in_minutes

    # Calculate difference in pages read
    diff_pages_read = dustin_pages_read - sam_pages_read
    result = diff_pages_read
    return result

print(solution())