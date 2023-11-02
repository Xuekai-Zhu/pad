def solution():
    notebooks = 5
    pages_per_notebook = 40
    pages_used_per_day = 4
    total_pages_used = notebooks * pages_used_per_day
    total_days = total_pages_used / pages_per_notebook
    result = total_days
    return result

print(solution())