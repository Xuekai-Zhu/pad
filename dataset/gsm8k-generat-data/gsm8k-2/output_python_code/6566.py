def solution():
    """John buys 5 notebooks that have 40 pages each. He uses 4 pages per day. How many days do the notebooks last?"""
    notebook_pages = 40
    notebooks = 5
    total_pages = notebook_pages * notebooks
    pages_used_per_day = 4
    days = total_pages / pages_used_per_day
    result = days
    return result

print(solution())