def solution():
    """Dustin and Sam are both reading. Dustin can read 75 pages in an hour. Sam can read 24 pages in an hour. How many more pages does Dustin read in 40 minutes compared to Sam?"""
    dustin_pages_per_minute = 75 / 60
    sam_pages_per_minute = 24 / 60
    dustin_pages_in_40_min = dustin_pages_per_minute * 40
    sam_pages_in_40_min = sam_pages_per_minute * 40
    pages_difference = dustin_pages_in_40_min - sam_pages_in_40_min
    result = pages_difference
    return result

print(solution())