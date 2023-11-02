def solution():
    """Léa bought one book for $16, three binders for $2 and six notebooks for $1. Calculate the total cost of her purchases."""
    # Define the cost of each item
    BOOK_COST = 16
    BINDER_COST = 2
    NOTEBOOK_COST = 1

    # Define the number of each item purchased
    num_books = 1
    num_binders = 3
    num_notebooks = 6

    # Calculate the total cost
    total_cost = num_books * BOOK_COST + num_binders * BINDER_COST + num_notebooks * NOTEBOOK_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())