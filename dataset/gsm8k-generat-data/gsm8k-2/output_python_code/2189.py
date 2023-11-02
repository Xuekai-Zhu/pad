def solution():
    """Jenny signs up for dinner theater with 5 of her friends. Each person pays $50 for the ticket and $10 for their entrée, and half the people also buy unlimited drink tickets for $30/person. Then the dinner theater is canceled due to COVID, and each person gets a 90% refund. How much money did the group of six friends lose?"""
    ticket_price = 50
    entree_price = 10
    drink_price = 30
    num_friends = 6
    num_drinkers = num_friends // 2

    total_cost = (ticket_price + entree_price + drink_price*num_drinkers)*num_friends
    refund = 0.9 * total_cost
    lost_money = total_cost - refund

    result = lost_money
    return result

print(solution())