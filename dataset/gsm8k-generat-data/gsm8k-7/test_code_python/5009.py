def solution():
    book_cost = 16
    num_binders = 3
    binder_cost = 2
    num_notebooks = 6
    notebook_cost = 1

    # Calculate the total cost of binders
    total_binder_cost = num_binders * binder_cost

    # Calculate the total cost of notebooks
    total_notebook_cost = num_notebooks * notebook_cost

    # Calculate the total cost of all purchases
    total_cost = book_cost + total_binder_cost + total_notebook_cost
    result = total_cost
    return result

print(solution())