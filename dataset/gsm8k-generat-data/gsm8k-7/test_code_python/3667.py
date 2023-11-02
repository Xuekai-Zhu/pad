def solution():
    total_pages = 100
    pages_read_3nights_ago = 15
    pages_read_2nights_ago = 2 * pages_read_3nights_ago
    pages_read_last_night = pages_read_2nights_ago + 5
    pages_left_to_read = total_pages - (pages_read_3nights_ago + pages_read_2nights_ago + pages_read_last_night)
    result = pages_left_to_read
    return result

print(solution())