def solution():
    """James buys 2 notebooks with 50 pages each. He pays $5. How many cents did each page cost?"""
    # Define the number of notebooks and pages per notebook
    notebooks = 2
    pages_per_notebook = 50

    # Define the total cost in cents and calculate the cost per page
    total_cost_cents = 500  # $5 in cents
    cost_per_page_cents = total_cost_cents / (notebooks * pages_per_notebook)

    # Display the cost per page
    result = cost_per_page_cents
    return result

print(solution())