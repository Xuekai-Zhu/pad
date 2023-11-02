def solution():
    num_basketball_packs = 2
    basketball_pack_price = 3

    num_baseball_decks = 5
    baseball_deck_price = 4

    total_cost = (num_basketball_packs * basketball_pack_price) + (num_baseball_decks * baseball_deck_price)
    amount_paid = 50

    # Calculate the amount of change Olivia received
    change = amount_paid - total_cost
    result = change
    return result

print(solution())