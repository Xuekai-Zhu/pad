def solution():
    # Calculate the total number of pages
    total_pages = 5 * 40

    # Calculate the number of pages John uses
    pages_used = 4 * days_used

    # Calculate the number of days the notebooks last
    days_used = total_pages / pages_used
    result = days_used
    return result

print(solution())