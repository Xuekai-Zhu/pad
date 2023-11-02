def solution():
    
    basketball_card_price = 3
    baseball_card_price = 4
    basketball_card_packs = 2
    baseball_card_decks = 5
    total_cost = (basketball_card_price * basketball_card_packs) + (baseball_card_price * baseball_card_decks)
    change = 50 - total_cost
    result = change
    return result

print(solution())