def solution():
    book_cost = 16  # Cost of one book
    binder_cost = 2  # Cost of one binder
    notebook_cost = 1  # Cost of one notebook
    num_binders = 3  # Number of binders Léa bought
    num_notebooks = 6  # Number of notebooks Léa bought

    # Calculate the total cost of Léa's purchases
    total_cost = book_cost + (binder_cost * num_binders) + (notebook_cost * num_notebooks)
    result = total_cost
    return result

print(solution())