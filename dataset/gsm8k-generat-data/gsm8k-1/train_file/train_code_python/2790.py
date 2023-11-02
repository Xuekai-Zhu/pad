def solution():
    """Violet is trying to figure out whether she should buy a family pass to the aquarium for $120 or pay for tickets separately. If adult tickets cost $35 and children's tickets cost $20, and Violet's family has 1 adult and 6 children, how much will she pay if she buys separate tickets?"""
    adult_ticket_cost = 35
    child_ticket_cost = 20
    num_adults = 1
    num_children = 6
    total_cost = (num_adults * adult_ticket_cost) + (num_children * child_ticket_cost)
    result = total_cost
    return result

print(solution())