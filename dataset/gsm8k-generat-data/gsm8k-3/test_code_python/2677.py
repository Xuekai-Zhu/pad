def solution():
    """Ten adults went to a ball game with eleven children. Adult tickets are $8 each and the total bill was $124. How many dollars is one child's ticket?"""
    # Define the number of adults and children and the total bill
    num_adults = 10
    num_children = 11
    total_bill = 124

    # Calculate the cost of the adult tickets
    adult_ticket_cost = num_adults * 8

    # Calculate the cost of the children's tickets
    children_ticket_cost = total_bill - adult_ticket_cost

    # Calculate the cost of one child's ticket
    cost_per_child = children_ticket_cost / num_children

    # Display the cost per child
    result = cost_per_child
    return result

print(solution())