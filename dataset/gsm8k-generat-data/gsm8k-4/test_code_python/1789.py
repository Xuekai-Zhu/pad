def solution():
    """Padma is trading cards with Robert. Padma started with 75 cards and traded 2 or her valuable ones for 10 of Robert's cards. Robert started with 88 of his own cards and traded another 8 of his cards for 15 of Padma's cards. How many cards were traded between both Padma and Robert?"""
    # Define the initial number of cards for Padma and Robert
    padma_cards = 75
    robert_cards = 88

    # Calculate the number of cards traded in the first trade
    padma_trade_1 = 2
    robert_trade_1 = 10

    # Update the number of cards for Padma and Robert after the first trade
    padma_cards -= padma_trade_1
    padma_cards += robert_trade_1
    robert_cards += padma_trade_1
    robert_cards -= robert_trade_1

    # Calculate the number of cards traded in the second trade
    padma_trade_2 = 15
    robert_trade_2 = 8

    # Update the number of cards for Padma and Robert after the second trade
    padma_cards += robert_trade_2
    robert_cards -= padma_trade_2

    # Calculate the total number of cards traded
    total_traded = padma_trade_1 + robert_trade_1 + padma_trade_2 + robert_trade_2

    result = total_traded
    return result

print(solution())