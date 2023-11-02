def solution():
    """Rob planned on spending three hours reading in preparation for his literature exam. If he ends up spending only three-quarters of this time reading, and he reads a page every fifteen minutes, how many pages did he read in this time?"""
    planned_reading_time = 3 * 60  # in minutes
    actual_reading_time = planned_reading_time * 0.75
    pages_per_minute = 1 / 15
    total_pages = int(pages_per_minute * actual_reading_time)
    result = total_pages
    return result

print(solution())