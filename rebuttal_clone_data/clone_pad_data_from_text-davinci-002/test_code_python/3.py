def solution():
     """Julie is reading a 120-page book. Yesterday, she was able to read 12 pages and today, she read twice as many pages as yesterday. If she wants to read half of the remaining pages tomorrow, how many pages should she read?"""
     total_pages = 120
     pages_read_yesterday = 12
     pages_read_today = pages_read_yesterday * 2
     pages_to_read_tomorrow = (total_pages - pages_read_today) / 2
     result = pages_to_read_tomorrow
     return result

print(solution())