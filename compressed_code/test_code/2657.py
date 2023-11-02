def solution():
    
    stamps_per_first_10_pages = 5 * 30 * 10
    stamps_per_remaining_pages = 50 * (50 - 10)
    total_stamps = stamps_per_first_10_pages + stamps_per_remaining_pages
    result = total_stamps
    return result

print(solution())