def solution():
    """Mark decides to buy packs of old magic cards and open them to sell. He buys 3 packs for $1800 each. He gets 1 card that is worth $4000 and another card worth $1000. There are 30 more cards worth an average of $50 each. How much money profit did he make?"""
    packs_bought = 3
    pack_cost = 1800
    cards_worth = 4000 + 1000
    total_cost = packs_bought * pack_cost
    additional_cards = 30
    average_card_worth = 50
    revenue = cards_worth + (additional_cards * average_card_worth)
    profit = revenue - total_cost
    result = profit
    return result

print(solution())