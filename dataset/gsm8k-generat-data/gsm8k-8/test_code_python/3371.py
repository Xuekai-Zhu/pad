def solution():
    # Calculate the total number of page increments across the five chapters
    total_increments = (5-1) * 3
    
    # Calculate the sum of the page numbers for all five chapters
    total_pages = 95
    
    # Calculate the page number for the first chapter
    first_chapter_pages = (total_pages - total_increments) / 5
    
    result = first_chapter_pages
    return result

print(solution())