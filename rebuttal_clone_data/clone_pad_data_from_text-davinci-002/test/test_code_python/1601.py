def solution():
    planned_hours = 3
    actual_hours = planned_hours * (3/4)
    minutes_per_page = 15
    pages_read = actual_hours * (60/minutes_per_page)
    result = pages_read
    return result

print(solution())