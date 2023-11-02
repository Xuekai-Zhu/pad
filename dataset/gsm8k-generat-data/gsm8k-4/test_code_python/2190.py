def solution():
    """Jenny signs up for dinner theater with 5 of her friends. Each person pays $50 for the ticket and $10 for their entrée, and half the people also buy unlimited drink tickets for $30/person. Then the dinner theater is canceled due to COVID, and each person gets a 90% refund. How much money did the group of six friends lose?"""
    # Calculate the total cost of tickets and meals
    ticket_cost = 6 * 50
    meal_cost = 6 * 10

    # Calculate the cost of drink tickets for half the group
    drink_cost = 3 * 30

    # Calculate the total cost including drink tickets
    total_cost = ticket_cost + meal_cost + drink_cost

    # Calculate the 90% refund
    refund = total_cost * 0.9

    # Calculate the amount of money lost
    money_lost = total_cost - refund

    result = money_lost
    return result

print(solution())