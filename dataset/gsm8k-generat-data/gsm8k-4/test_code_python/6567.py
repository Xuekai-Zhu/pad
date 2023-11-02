def solution():
    """John buys 5 notebooks that have 40 pages each. He uses 4 pages per day. How many days do the notebooks last?"""
    # Define the number of notebooks and pages per notebook
    num_notebooks = 5
    pages_per_notebook = 40

    # Calculate the total number of pages
    total_pages = num_notebooks * pages_per_notebook

    # Define the number of pages used per day
    pages_per_day = 4

    # Calculate the number of days the notebooks will last
    days_last = total_pages / pages_per_day

    result = days_last
    return result

print(solution())