def solution():
    pages_read_3_nights_ago = 15
    pages_read_2_nights_ago = pages_read_3_nights_ago * 2
    pages_read_1_night_ago = pages_read_2_nights_ago + 5
    total_pages = 100
    pages_to_read_tonight = total_pages - pages_read_1_night_ago
    result = pages_to_read_tonight
    return result

print(solution())