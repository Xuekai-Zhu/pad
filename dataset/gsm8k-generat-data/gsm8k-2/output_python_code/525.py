def solution():
    """On Monday, Mack writes in his journal for 60 minutes at a rate of 1 page every 30 minutes. On Tuesday, Mack writes in his journal for 45 minutes at a rate of 1 page every 15 minutes. On Wednesday, Mack writes 5 pages in his journal. How many pages total does Mack write in his journal from Monday to Wednesday?"""
    monday_pages = 60 / 30
    tuesday_pages = 45 / 15
    wednesday_pages = 5
    total_pages = monday_pages + tuesday_pages + wednesday_pages
    result = total_pages
    return result

print(solution())