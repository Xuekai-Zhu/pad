def solution():
    num_notebooks = 5
    pages_per_notebook = 40
    pages_used_per_day = 4

    # Calculate the total number of pages in all notebooks
    total_pages = num_notebooks * pages_per_notebook

    # Calculate the number of days the notebooks will last
    num_days = total_pages / pages_used_per_day
    result = num_days
    return result

print(solution())