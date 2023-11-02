def solution():
    rose_cups_per_hour = 6
    lily_cups_per_hour = 7
    rose_cups_ordered = 6
    lily_cups_ordered = 14
    total_cups = rose_cups_ordered + lily_cups_ordered
    total_time = total_cups / (rose_cups_per_hour + lily_cups_per_hour)
    hourly_rate = 90 / total_time
    result = hourly_rate
    return result

print(solution())