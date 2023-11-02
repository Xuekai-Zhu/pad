def solution():
    """Lola and Dora combined their allowance of $9 each to buy a deck of playing cards for $10, they also bought $2 boxes of stickers and split the boxes evenly. How many packs of stickers did Dora get?"""
    # Define the total allowance of Lola and Dora
    total_allowance = 9 + 9

    # Define the cost of the deck of playing cards and the boxes of stickers
    cards_cost = 10
    stickers_cost = 2

    # Calculate the total amount spent by Lola and Dora
    total_spent = cards_cost + stickers_cost

    # Calculate the amount left after buying the deck of playing cards and the boxes of stickers
    amount_left = total_allowance - total_spent

    # Calculate the number of packs of stickers they bought
    packs_of_stickers = stickers_cost / 2

    # Calculate the number of packs of stickers Dora got
    dora_stickers = packs_of_stickers / 2

    result = dora_stickers
    return result

print(solution())