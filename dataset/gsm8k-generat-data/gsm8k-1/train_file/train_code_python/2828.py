def solution():
    """Rob planned on spending three hours reading in preparation for his literature exam. If he ends up spending only three-quarters of this time reading, and he reads a page every fifteen minutes, how many pages did he read in this time?"""
    planned_time = 3 # hours
    actual_time = planned_time * 0.75 # hours
    time_per_page = 15 # minutes
    pages_read = actual_time * 60 / time_per_page
    result = pages_read
    return result

print(solution())