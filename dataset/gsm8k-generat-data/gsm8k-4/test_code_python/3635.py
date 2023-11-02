def solution():
    """Mike spent 37 dollars on notebooks. He bought a total of 12 notebooks. He bought 3 red notebooks at 4 dollars each, 2 green notebooks at 2 dollars each, and the rest were blue notebooks. How much does each blue notebook cost?"""
    # Define the total amount spent and the number of notebooks bought
    total_spent = 37
    total_notebooks = 12

    # Calculate the cost of the red notebooks
    red_cost = 3 * 4

    # Calculate the cost of the green notebooks
    green_cost = 2 * 2

    # Calculate the total cost of the blue notebooks
    blue_cost = total_spent - red_cost - green_cost

    # Calculate the cost of each blue notebook
    blue_cost_per_notebook = blue_cost / (total_notebooks - 3 - 2)

    # Return the result
    result = blue_cost_per_notebook
    return result

print(solution())