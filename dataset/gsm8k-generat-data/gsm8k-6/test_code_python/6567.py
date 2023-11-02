def solution():
    # Calculate the total number of pages in the notebooks
    total_pages = 5 * 40  # 5 notebooks with 40 pages each

    # Calculate how many days the notebooks will last
    days_last = total_pages // 4  # each day uses 4 pages
    result = days_last
    return result

print(solution())