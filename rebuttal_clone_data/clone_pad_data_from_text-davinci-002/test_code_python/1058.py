def solution():
    hours_read_per_day = 10
    days_read = 5
    pages_read_per_hour = 50
    total_hours = hours_read_per_day * days_read
    total_pages_read = total_hours * pages_read_per_hour
    result = total_pages_read
    return result

print(solution())