def solution():
    """Dustin can read 75 pages in an hour. Sam can read 24 pages in an hour. How many more pages does Dustin read in 40 minutes compared to Sam?"""
    dustin_rate = 75 / 60
    sam_rate = 24 / 60
    dustin_pages = dustin_rate * 40
    sam_pages = sam_rate * 40
    more_pages = dustin_pages - sam_pages
    result = more_pages
    return result

print(solution())