def solution():
    pages_counted = 50
    stamps_per_page_first_ten = 5 * 30
    stamps_per_page_rest = 50
    total_stamps = stamps_per_page_first_ten + (pages_counted - 10) * stamps_per_page_rest
    result = total_stamps
    return result

print(solution())