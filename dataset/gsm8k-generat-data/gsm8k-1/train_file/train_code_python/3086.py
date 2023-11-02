def solution():
    """While planning to finish reading a 140-page book in one week, Jessy initially decides to read 3 times daily, 6 pages each time, every day of the week. How many more pages should she read per day to actually achieve her goal?"""
    total_pages = 140
    pages_per_day_initial = 3 * 6
    days_to_finish = 7
    pages_per_day_needed = total_pages / days_to_finish
    pages_extra_per_day = pages_per_day_needed - pages_per_day_initial
    result = pages_extra_per_day
    return result

print(solution())