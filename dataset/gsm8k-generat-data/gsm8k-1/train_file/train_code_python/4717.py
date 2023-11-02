def solution():
    """James writes from 1 PM to 4 PM every night. He can write 5 pages per hour. How many weeks will it take to finish his 735-page book?"""
    start_time = 1
    end_time = 4
    hours_per_night = end_time - start_time
    daily_page_output = hours_per_night * 5
    total_pages = 735
    weeks_needed = total_pages // daily_page_output
    result = weeks_needed
    return result

print(solution())