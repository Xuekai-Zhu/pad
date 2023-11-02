def solution():
    """A notebook costs three times as much as a pen. If a pen costs $1.50, how much will Lyle pay for 4 notebooks?"""
    # Define the cost of a pen
    PEN_PRICE = 1.5

    # Define the cost of a notebook relative to a pen
    NOTEBOOK_PRICE = 3 * PEN_PRICE

    # Calculate the total cost of 4 notebooks
    total_cost = 4 * NOTEBOOK_PRICE

    # Display the total cost
    result = total_cost
    return result

print(solution())