def solution():
    
    total_pages = 100
    pages_read_first_night = 15
    pages_read_second_night = 2 * pages_read_first_night
    pages_read_third_night = pages_read_second_night + 5
    pages_read_so_far = pages_read_first_night + pages_read_second_night + pages_read_third_night
    pages_left_to_read = total_pages - pages_read_so_far
    result = pages_left_to_read
    return result

print(solution())