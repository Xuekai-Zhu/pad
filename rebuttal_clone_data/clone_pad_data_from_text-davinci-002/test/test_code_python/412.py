def solution():
     pages_read_first_week = 600 / 2
     pages_read_second_week = (600 - pages_read_first_week) * 0.3
     pages_read_third_week = 600 - pages_read_first_week - pages_read_second_week
     result = pages_read_third_week
     return result

print(solution())