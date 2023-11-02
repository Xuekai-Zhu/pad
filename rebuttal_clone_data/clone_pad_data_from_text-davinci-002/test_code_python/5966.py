def solution():
    total_pages = 500
    pages_read_first_night = total_pages * 0.2
    pages_read_second_night = total_pages * 0.2
    pages_read_third_night = total_pages * 0.3
    pages_left = total_pages - (pages_read_first_night + pages_read_second_night + pages_read_third_night)
    result = pages_left
    return result

print(solution())