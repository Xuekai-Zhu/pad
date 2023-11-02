def solution():
    """Becca, Smendrick, and PJ have collections of Magic Cards. There is a total of 341 cards. Becca has 12 more than Smendrick, and Smendrick has 3 times the amount of cards that PJ has. How many cards does Becca have?"""
    total_cards = 341
    cards_pj = total_cards / 10
    cards_smendrick = cards_pj * 3
    cards_becca = cards_smendrick + 12
    result = cards_becca
    return result

print(solution())