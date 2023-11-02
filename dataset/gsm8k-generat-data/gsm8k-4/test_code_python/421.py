def solution():
    """Mrs. Wilsborough saved $500 to buy concert tickets for her family. She bought 2 VIP tickets at $100 each and 3 regular tickets at $50 each. How much of her savings does Mrs. Wilsborough have after she buys the tickets?"""
    # Define the cost of VIP and regular tickets
    VIP_TICKET_COST = 100
    REGULAR_TICKET_COST = 50

    # Define the number of VIP and regular tickets purchased
    num_VIP_tickets = 2
    num_regular_tickets = 3

    # Calculate the total cost of the tickets
    total_cost = (VIP_TICKET_COST * num_VIP_tickets) + (REGULAR_TICKET_COST * num_regular_tickets)

    # Calculate the amount left from her savings
    savings_left = 500 - total_cost

    result = savings_left
    return result

print(solution())