def solution():
    planned_reading_time = 3  # hours
    actual_reading_time = planned_reading_time * 0.75  # 75% of planned time
    pages_per_minute = 4  # 1 page every 15 minutes

    # Calculate the total number of pages Rob read
    total_pages_read = int(actual_reading_time * 60 * pages_per_minute)
    result = total_pages_read
    return result

print(solution())