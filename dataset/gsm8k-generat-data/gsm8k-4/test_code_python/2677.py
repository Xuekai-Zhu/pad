def solution():
    """Ten adults went to a ball game with eleven children. Adult tickets are $8 each and the total bill was $124. How many dollars is one child's ticket?"""
    # Define the number of adults and children
    num_adults = 10
    num_children = 11

    # Define the price of an adult ticket and the total bill
    adult_price = 8
    total_bill = 124

    # Calculate the total cost of the adult tickets
    adult_cost = num_adults * adult_price

    # Calculate the total cost of the children's tickets
    children_cost = total_bill - adult_cost

    # Calculate the price of one child's ticket
    child_price = children_cost / num_children

    # return the result
    result = child_price
    return result

print(solution())