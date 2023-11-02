def solution():
     days_in_week = 7
     weeks_in_month = 4
     pages_read_by_janet = 80
     pages_read_by_belinda = 30
     janet_reads_in_month = days_in_week * weeks_in_month * pages_read_by_janet
     belinda_reads_in_month = days_in_week * weeks_in_month * pages_read_by_belinda
     difference_in_pages = janet_reads_in_month - belinda_reads_in_month
     result = difference_in_pages
     return result

print(solution())