def solution():
    initial_pages_read = 10
    pages_to_read = 100
    remaining_days = 6
    pages_read_per_day = initial_pages_read * 2
    total_pages_read = pages_read_per_day * remaining_days + initial_pages_read
    result = total_pages_read
    
    return result

print(solution())