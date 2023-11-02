def solution():
    """Mrs. Wilsborough saved $500 to buy concert tickets for her family. She bought 2 VIP tickets at $100 each and 3 regular tickets at $50 each. How much of her savings does Mrs. Wilsborough have after she buys the tickets?"""
    # Define the cost of each type of ticket
    VIP_PRICE = 100
    REGULAR_PRICE = 50

    # Define the number of VIP and regular tickets purchased
    num_vip_tickets = 2
    num_regular_tickets = 3

    # Calculate the total cost of the VIP tickets
    vip_cost = num_vip_tickets * VIP_PRICE

    # Calculate the total cost of the regular tickets
    regular_cost = num_regular_tickets * REGULAR_PRICE

    # Calculate the total cost of all the tickets
    total_cost = vip_cost + regular_cost

    # Calculate the amount of savings Mrs. Wilsborough has left after buying the tickets
    remaining_savings = 500 - total_cost

    # Display the remaining savings
    result = remaining_savings
    return result

print(solution())