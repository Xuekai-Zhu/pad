def solution():
     goal_pages = 600
     days_in_month = 30
     pages_read_on_13th = 0
     pages_read_on_23rd = 100
     days_left = days_in_month - (4 + 1 + 1)
     pages_left = goal_pages - (pages_read_on_13th + pages_read_on_23rd)
     pages_per_day = pages_left / days_left
     result = pages_per_day
     return result

print(solution())