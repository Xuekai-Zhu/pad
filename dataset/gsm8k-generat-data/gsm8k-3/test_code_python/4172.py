def solution():
    """Nine adults went to a play with seven children. Adult tickets are $11 each and children's tickets are $7 each. How many dollars more did the adults' tickets cost in total than the children's tickets in total?"""
    # Define the cost of each type of ticket
    ADULT_PRICE = 11
    CHILD_PRICE = 7

    # Define the number of adults and children
    num_adults = 9
    num_children = 7

    # Calculate the total cost of the adults' tickets
    adult_cost = num_adults * ADULT_PRICE

    # Calculate the total cost of the children's tickets
    child_cost = num_children * CHILD_PRICE

    # Calculate the difference in cost between the adults' and children's tickets
    diff_cost = adult_cost - child_cost

    # Display the difference in cost
    result = diff_cost
    return result

print(solution())