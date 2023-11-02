def solution():
    pages_per_notebook = 40  # Each notebook has 40 pages
    total_pages = pages_per_notebook * 5  # John buys 5 notebooks
    pages_used_per_day = 4  # John uses 4 pages per day

    # Calculate the number of days the notebooks will last
    days_lasting = total_pages // pages_used_per_day
    result = days_lasting
    return result

print(solution())