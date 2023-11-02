def solution():
    """Padma is trading cards with Robert. Padma started with 75 cards and traded 2 or her valuable ones for 10 of Robert's cards. Robert started with 88 of his own cards and traded another 8 of his cards for 15 of Padma's cards. How many cards were traded between both Padma and Robert?"""
    # Padma's starting number of cards
    padma_start = 75

    # Robert's starting number of cards
    robert_start = 88

    # Number of cards Padma traded for Robert's cards
    padma_trade = 2
    robert_trade = 10

    # Number of cards Robert traded for Padma's cards
    robert_trade_2 = 8
    padma_trade_2 = 15

    # Total number of cards traded
    total_cards_traded = padma_trade + robert_trade + robert_trade_2 + padma_trade_2

    # Display the total number of cards traded
    result = total_cards_traded
    return result

print(solution())