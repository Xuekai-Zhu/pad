def solution():
    """Jenny signs up for dinner theater with 5 of her friends. Each person pays $50 for the ticket and $10 for their entrée, and half the people also buy unlimited drink tickets for $30/person. Then the dinner theater is canceled due to COVID, and each person gets a 90% refund. How much money did the group of six friends lose?"""
    # Define the cost of the ticket, entrée, and drink ticket
    TICKET_PRICE = 50
    ENTREE_PRICE = 10
    DRINK_PRICE = 30

    # Define the number of people in the group
    group_size = 6

    # Calculate the total cost per person
    total_cost_per_person = TICKET_PRICE + ENTREE_PRICE
    if group_size % 2 == 0:
        total_cost_per_person += DRINK_PRICE

    # Calculate the total cost for the group
    total_cost = total_cost_per_person * group_size

    # Calculate the refund amount per person
    refund_amount = total_cost_per_person * 0.9

    # Calculate the total refund amount for the group
    total_refund = refund_amount * group_size

    # Calculate the amount the group lost
    amount_lost = total_cost - total_refund

    # Display the amount the group lost
    result = amount_lost
    return result

print(solution())