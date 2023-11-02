def solution():
    
    dustin_pages_per_minute = 75 / 60
    sam_pages_per_minute = 24 / 60
    dustin_pages_in_40_min = dustin_pages_per_minute * 40
    sam_pages_in_40_min = sam_pages_per_minute * 40
    pages_difference = dustin_pages_in_40_min - sam_pages_in_40_min
    result = pages_difference
    return result

print(solution())