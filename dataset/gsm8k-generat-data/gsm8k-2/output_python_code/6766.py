def solution():
    """Jenna sets a goal of reading 600 pages a month for the month of September (which has 30 days). She knows that she'll be really busy at work the four weekdays starting on the 13th, so she won't have time to read. She can also read 100 pages on the 23rd, when she'll have a long boring flight. If she reads the same number of pages every other day, how many pages a day does she need to read?"""
    total_pages = 600
    days_available = 30 - 4 - 1  # subtract 4 weekdays and the day she'll be busy on the 23rd
    remaining_pages = total_pages - 100  # subtract the pages she'll read on the 23rd
    pages_per_day = remaining_pages / days_available
    result = pages_per_day
    return result

print(solution())