def solution():
    """Jenna sets a goal of reading 600 pages a month for the month of September (which has 30 days). She knows that she'll be really busy at work the four weekdays starting on the 13th, so she won't have time to read. She can also read 100 pages on the 23rd, when she'll have a long boring flight. If she reads the same number of pages every other day, how many pages a day does she need to read?"""
    
    # Total number of days excluding the 4 weekdays starting from the 13th but including the 23rd
    days_available = 30 - 4 + 1
    
    # Total number of pages to be read excluding the 100 pages on the 23rd
    total_pages_to_be_read = 600 - 100
    
    # Number of pages Jenna needs to read every other day
    daily_pages_to_be_read = total_pages_to_be_read / (days_available - 1)
    
    result = daily_pages_to_be_read
    
    return result

print(solution())