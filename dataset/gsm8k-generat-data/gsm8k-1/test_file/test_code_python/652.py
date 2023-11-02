def solution():
    """Mike's teacher, leaves as homework the reading of a 200-page book. The assignment is to be completed within 30 days. Mike plans to read 10 pages a day. How many days before the deadline will Mike finish his reading?"""
    total_pages = 200
    days_to_complete = 30
    pages_per_day = 10
    pages_left = total_pages
    days_left = 0
    while pages_left > 0:
        pages_left -= pages_per_day
        days_left += 1
    result = days_to_complete - days_left
    return result

print(solution())