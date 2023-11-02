def solution():
    """Violet is trying to figure out whether she should buy a family pass to the aquarium for $120 or pay for tickets separately. If adult tickets cost $35 and children's tickets cost $20, and Violet's family has 1 adult and 6 children, how much will she pay if she buys separate tickets?"""
    # Define the number of adults and children in Violet's family
    num_adults = 1
    num_children = 6

    # Define the cost of the family pass
    family_pass_cost = 120

    # Define the cost of buying separate tickets
    adult_ticket_cost = 35
    children_ticket_cost = 20

    # Calculate the total cost of buying separate tickets for Violet's family
    total_cost = num_adults * adult_ticket_cost + num_children * children_ticket_cost

    # Check if buying the family pass is cheaper than buying separate tickets
    if family_pass_cost < total_cost:
        result = family_pass_cost
    else:
        result = total_cost
    return result

print(solution())