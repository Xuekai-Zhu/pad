def solution():
    """Mike spent 37 dollars on notebooks. He bought a total of 12 notebooks. He bought 3 red notebooks at 4 dollars each, 2 green notebooks at 2 dollars each, and the rest were blue notebooks. How much does each blue notebook cost?"""
    # Calculate the total cost of the red notebooks
    red_cost = 3 * 4

    # Calculate the total cost of the green notebooks
    green_cost = 2 * 2

    # Calculate the total cost of all the notebooks
    total_cost = 37
    total_notebooks = 12
    blue_notebooks = total_notebooks - 3 - 2
    blue_cost = (total_cost - red_cost - green_cost) / blue_notebooks

    # Display the cost of each blue notebook
    result = blue_cost
    return result

print(solution())