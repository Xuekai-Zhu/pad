def solution():
    """Theo has $6000 he wishes to spend on his upcoming business trip to South Africa. He buys 6 business suits at $100 each, 3 suitcases at $50 each, a flight ticket that costs $700 more than 5 times as much as the cost of a business suit.
    He wishes to save $2000 for this trip, how much does he have to spend on buying gifts for his business partners in South Africa?"""
    
    # Cost of 6 business suits
    suits_cost = 6 * 100
    
    # Cost of 3 suitcases
    suitcase_cost = 3 * 50
    
    # Cost of one business suit
    suit_cost = suits_cost / 6
    
    # Cost of flight ticket
    flight_ticket_cost = 5 * suit_cost + 700
    
    # Total cost of everything
    total_cost = suits_cost + suitcase_cost + flight_ticket_cost
    
    # Amount to save
    amount_to_save = 2000
    
    # Amount to spend on gifts
    amount_for_gifts = 6000 - total_cost - amount_to_save
    
    result = amount_for_gifts
    
    return result

print(solution())