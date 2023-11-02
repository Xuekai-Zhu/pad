def solution():
    """Berry wants to make sure he reads an average of 50 pages a day. This week he read 43 pages on Sunday, 65 pages on Monday, and 28 pages on Tuesday. He had a soccer game and fell asleep early on Wednesday so he read nothing. On Thursday he read 70 pages, and on Friday he read 56 pages. How many pages does he have to read on Saturday to reach his goal?"""
    goal_pages_per_week = 7 * 50
    total_pages_read = 43 + 65 + 28 + 0 + 70 + 56
    pages_left_to_read = goal_pages_per_week - total_pages_read
    result = pages_left_to_read
    return result

print(solution())