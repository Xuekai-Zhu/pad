def solution():
    """John buys 5 notebooks that have 40 pages each. He uses 4 pages per day. How many days do the notebooks last?"""
    notebooks = 5
    pages = 40
    pages_used_per_day = 4
    total_pages_used = pages_used_per_day * 7  # assuming he uses it 7 days a week
    days_last = (notebooks * pages) / total_pages_used
    result = days_last
    return result

print(solution())