def solution():
    """Nina wants to give presents to her children. She buys three toys at $10 each, two packs of basketball cards at $5 each, and five shirts at $6 each. How much does she spend in all?"""
    toy_cost = 10
    basketball_cards_cost = 5
    shirt_cost = 6
    num_of_toys = 3
    num_of_basketball_cards = 2
    num_of_shirts = 5
    total_cost = (toy_cost * num_of_toys) + (basketball_cards_cost * num_of_basketball_cards) + (shirt_cost * num_of_shirts)
    result = total_cost
    return result

print(solution())