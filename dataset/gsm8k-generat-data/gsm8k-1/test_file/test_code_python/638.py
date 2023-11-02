def solution():
    """James buys a new wardrobe. He buys 10 suits and 10 dress pants. He also buys 3 dress shirts per suit. The suits cost $750 each and the dress pants cost 1/5 that cost. The dress shirts were $60 each. How much did everything cost?"""
    num_suits = 10
    num_pants = 10
    num_shirts = 3 * num_suits
    suit_cost = 750
    pant_cost = suit_cost / 5
    shirt_cost = 60
    total_cost = (num_suits * suit_cost) + (num_pants * pant_cost) + (num_shirts * shirt_cost)
    result = total_cost
    return result

print(solution())