def solution():
    
    pages_1 = 2
    pages_2 = 3
    pages_3 = 1
    count_1 = 5
    count_2 = 5
    count_3 = 5
    total_pages = (pages_1 * count_1) + (pages_2 * count_2) + (pages_3 * count_3)
    average_page_count = total_pages / 15
    result = average_page_count
    return result

print(solution())