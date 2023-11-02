def solution():
    """Ethan is reading a sci-fi book that has 360 pages. He read 40 pages on Saturday morning and another 10 pages at night. The next day he read twice the total pages as on Saturday. How many pages does he have left to read?"""
    
    # Define the number of pages in the book and the pages read on Saturday and Sunday
    total_pages = 360
    saturday_pages = 40 + 10  # Total pages read on Saturday
    sunday_pages = 2 * saturday_pages  # Total pages read on Sunday
    
    # Calculate the pages left to read
    pages_left = total_pages - (saturday_pages + sunday_pages)
    
    result = pages_left
    return result

print(solution())