def solution():
    """Six kids and two adults are going to the circus. Kid's tickets are on sale for only half of the adult tickets. The total cost is $50. How much is one kid's ticket?"""
    num_kids = 6
    num_adults = 2
    total_tickets = num_kids + num_adults
    total_cost = 50
    cost_per_adult = total_cost / total_tickets
    cost_per_kid = cost_per_adult / 2
    result = cost_per_kid
    return result

print(solution())