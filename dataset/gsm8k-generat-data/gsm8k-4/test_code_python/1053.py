def solution():
    """Jane plans on reading a novel she borrows from her friend. She reads twice a day, once in the morning and once in the evening. In the morning she reads 5 pages and in the evening she reads 10 pages. If she reads at this rate for a week, how many pages will she read?"""
    # Define the number of pages read in the morning and evening
    MORNING_PAGES = 5
    EVENING_PAGES = 10

    # Define the number of days
    days = 7

    # Calculate the total number of pages read in a day
    daily_pages = MORNING_PAGES + EVENING_PAGES

    # Calculate the total number of pages read in a week
    weekly_pages = daily_pages * 2 * days

    result = weekly_pages
    return result

print(solution())