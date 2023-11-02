def solution():
    last_week_pages = 5 * 300  # pages read last week
    this_week_pages = last_week_pages * 2  # pages read this week (twice as much as last week)
    total_pages = last_week_pages + this_week_pages  # total pages read
    result = total_pages
    return result

print(solution())