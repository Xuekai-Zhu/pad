def solution():
    """James buys 2 notebooks with 50 pages each. He pays $5. How many cents did each page cost?"""
    # Define the number of notebooks and pages per notebook
    num_notebooks = 2
    pages_per_notebook = 50

    # Define the total cost in cents
    total_cost = 500  # $5 = 500 cents

    # Calculate the cost per page
    cost_per_page = total_cost / (num_notebooks * pages_per_notebook)

    # Convert to cents per page
    cents_per_page = cost_per_page * 100

    # Return the result
    result = cents_per_page
    return result

print(solution())