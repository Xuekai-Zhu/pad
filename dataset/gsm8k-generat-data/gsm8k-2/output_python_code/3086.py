def solution():
    """While planning to finish reading a 140-page book in one week, Jessy initially decides to read 3 times daily, 6 pages each time, every day of the week. How many more pages should she read per day to actually achieve her goal?"""
    page_goal = 140
    initial_pages_per_day = 3 * 6
    initial_total_pages = initial_pages_per_day * 7
    remaining_pages = page_goal - initial_total_pages
    additional_pages_per_day = remaining_pages / 7
    result = additional_pages_per_day
    return result

print(solution())