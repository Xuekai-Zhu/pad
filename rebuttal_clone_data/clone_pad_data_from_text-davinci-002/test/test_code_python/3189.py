def solution():
    dustin_pages_per_hour = 75
    sam_pages_per_hour = 24
    time_in_minutes = 40
    time_in_hours = time_in_minutes / 60
    dustin_total_pages = dustin_pages_per_hour * time_in_hours
    sam_total_pages = sam_pages_per_hour * time_in_hours
    difference = dustin_total_pages - sam_total_pages
    result = difference
    return result

print(solution())