def solution():
    basketball_pack_price = 3  # The price of one pack of basketball cards is $3
    baseball_deck_price = 4  # The price of one deck of baseball cards is $4
    basketball_packs = 2  # Olivia bought 2 packs of basketball cards
    baseball_decks = 5  # Olivia bought 5 decks of baseball cards
    total_cost = (basketball_pack_price * basketball_packs) + (baseball_deck_price * baseball_decks)  # Calculate the total cost
    change = 50 - total_cost  # Subtract the total cost from the $50 bill Olivia had

    result = change
    return result

print(solution())