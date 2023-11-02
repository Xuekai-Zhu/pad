def solution():
    """Berry wants to make sure he reads an average of 50 pages a day. This week he read 43 pages on Sunday, 65 pages on Monday, and 28 pages on Tuesday. He had a soccer game and fell asleep early on Wednesday so he read nothing. On Thursday he read 70 pages, and on Friday he read 56 pages. How many pages does he have to read on Saturday to reach his goal?"""
    goal = 50 * 7 # 7 days in a week
    pages_read = 43 + 65 + 28 + 0 + 70 + 56
    pages_left = goal - pages_read
    result = pages_left
    return result

print(solution())