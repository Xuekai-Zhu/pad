def solution():
    """On Monday, Mack writes in his journal for 60 minutes at a rate of 1 page every 30 minutes. On Tuesday, Mack writes in his journal for 45 minutes at a rate of 1 page every 15 minutes. On Wednesday, Mack writes 5 pages in his journal. How many pages total does Mack write in his journal from Monday to Wednesday?"""
    # Define the number of pages written on Monday
    pages_monday = 60 // 30

    # Define the number of pages written on Tuesday
    pages_tuesday = 45 // 15

    # Define the number of pages written on Wednesday
    pages_wednesday = 5

    # Calculate the total number of pages written
    total_pages = pages_monday + pages_tuesday + pages_wednesday

    result = total_pages
    return result

print(solution())