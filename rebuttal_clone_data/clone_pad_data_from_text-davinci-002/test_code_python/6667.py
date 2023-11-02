def solution():
    pages_written = 6
    time_researching = 45
    time_editing = 75
    time_per_page = 30
    total_time = (pages_written * time_per_page) + time_researching + time_editing
    result = total_time
    return result

print(solution())