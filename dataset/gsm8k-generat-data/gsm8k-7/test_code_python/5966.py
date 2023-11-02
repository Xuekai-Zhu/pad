def solution():
    total_pages = 500
    percent_1 = 0.2 
    percent_2 = 0.2
    percent_3 = 0.3
    pages_read_1 = total_pages * percent_1
    pages_read_2 = total_pages * percent_2
    pages_read_3 = total_pages * percent_3
    pages_left = total_pages - pages_read_1 - pages_read_2 - pages_read_3
    result = pages_left
    return result

print(solution())