def solution():
    """James writes from 1 PM to 4 PM every night. He can write 5 pages per hour. How many weeks will it take to finish his 735-page book?"""
    writing_hours_per_night = 3
    pages_per_hour = 5
    total_pages = 735
    total_writing_hours = total_pages / pages_per_hour
    total_writing_weeks = total_writing_hours / (5 * writing_hours_per_night)
    result = total_writing_weeks
    return result

print(solution())