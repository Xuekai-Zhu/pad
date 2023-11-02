def solution():
    """Violet is trying to figure out whether she should buy a family pass to the aquarium for $120 or pay for tickets separately. If adult tickets cost $35 and children's tickets cost $20, and Violet's family has 1 adult and 6 children, how much will she pay if she buys separate tickets?"""
    # Define the cost of each type of ticket
    ADULT_TICKET = 35
    CHILD_TICKET = 20

    # Define the number of adults and children in Violet's family
    num_adults = 1
    num_children = 6

    # Calculate the cost of all the adult tickets
    adult_cost = num_adults * ADULT_TICKET

    # Calculate the cost of all the children's tickets
    children_cost = num_children * CHILD_TICKET

    # Calculate the total cost of all the tickets
    total_cost = adult_cost + children_cost

    # Check if buying a family pass is cheaper
    if total_cost > 120:
        result = "Buy the family pass for $120"
    else:
        result = total_cost

    return result

print(solution())