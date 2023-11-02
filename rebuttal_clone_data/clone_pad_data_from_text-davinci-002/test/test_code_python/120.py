def solution():
     
     total_pages = 408
     pages_read = 113
     days_left = 5
     pages_per_day = (total_pages - pages_read) / days_left
     result = pages_per_day
     return result

print(solution())