def solution():
    # Calculate the total number of pages Juwella has read so far
    total_pages_read = 15 + 2*15 + (2*15 + 5)  # three nights ago she read 15 pages, two nights ago she read twice that amount (30), last night she read 5 more pages (35)
    
    # Calculate the number of pages remaining to be read
    pages_remaining = 100 - total_pages_read
    
    result = pages_remaining
    return result

print(solution())