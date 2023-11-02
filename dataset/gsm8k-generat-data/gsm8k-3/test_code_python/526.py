def solution():
    """On Monday, Mack writes in his journal for 60 minutes at a rate of 1 page every 30 minutes. On Tuesday, Mack writes in his journal for 45 minutes at a rate of 1 page every 15 minutes. On Wednesday, Mack writes 5 pages in his journal. How many pages total does Mack write in his journal from Monday to Wednesday?"""
    # Calculate the number of pages Mack writes on Monday
    pages_monday = 60 / 30

    # Calculate the number of pages Mack writes on Tuesday
    pages_tuesday = 45 / 15

    # Calculate the total number of pages Mack writes
    total_pages = pages_monday + pages_tuesday + 5

    # Display the total number of pages
    result = total_pages
    return result

print(solution())