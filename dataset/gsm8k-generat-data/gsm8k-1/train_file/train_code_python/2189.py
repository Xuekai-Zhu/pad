def solution():
    """Jenny signs up for dinner theater with 5 of her friends. Each person pays $50 for the ticket and $10 for their entrée, and half the people also buy unlimited drink tickets for $30/person. Then the dinner theater is canceled due to COVID, and each person gets a 90% refund. How much money did the group of six friends lose?"""
    num_people = 6
    ticket_cost = 50
    entree_cost = 10
    drink_cost = 30
    num_drinkers = num_people // 2

    total_cost = num_people * (ticket_cost + entree_cost) + num_drinkers * drink_cost
    refund = total_cost * 0.9
    loss = total_cost - refund
    result = loss
    
    return result

print(solution())