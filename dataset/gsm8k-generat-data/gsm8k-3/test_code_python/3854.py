def solution():
    """Sara's sister has 4 small notebooks in her closet. Last summer she ordered 6 more notebooks and then lost 2. How many notebooks does Sara's sister have now?"""
    # Define the initial number of notebooks
    initial_notebooks = 4

    # Define the number of notebooks ordered and lost
    notebooks_ordered = 6
    notebooks_lost = 2

    # Calculate the current number of notebooks
    current_notebooks = initial_notebooks + notebooks_ordered - notebooks_lost

    # Display the current number of notebooks
    result = current_notebooks
    return result

print(solution())