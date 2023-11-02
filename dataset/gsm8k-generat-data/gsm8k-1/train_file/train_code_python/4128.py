def solution():
    """Jeremie wants to go to an amusement park with 3 friends at the end of summer. Tickets are $18 for children and a set of snack cost $5. How much will it cost Jeremie and her 3 friends to go to the amusement park and buy each of them a set of snacks?"""
    num_friends = 3
    ticket_cost = 18
    snack_cost = 5
    total_cost = (num_friends + 1) * (ticket_cost + snack_cost)
    result = total_cost
    return result

print(solution())