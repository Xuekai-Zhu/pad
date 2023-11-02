def solution():
     """Bekah had to read 408 pages for history class. She read 113 pages over the weekend and has 5 days left to finish her reading. How many pages will she need to read each day for 5 days to complete her assignment?"""
     total_pages = 408
     pages_read = 113
     days_left = 5
     pages_per_day = (total_pages - pages_read) / days_left
     result = pages_per_day
     return result

print(solution())