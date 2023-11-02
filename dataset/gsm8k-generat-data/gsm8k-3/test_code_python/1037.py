def solution():
    """John buys a gaming PC for $1200.  He decides to replace the video card in it. He sells the old card for $300 and buys a new one for $500.  How much money did he spend on his computer, counting the savings from selling the old card?"""
    # Define the cost of the computer, the amount received from selling the old card, and the cost of the new card
    COMPUTER_COST = 1200
    OLD_CARD_SALE_PRICE = 300
    NEW_CARD_COST = 500

    # Calculate the total cost of the computer after selling the old card and buying the new card
    total_cost = COMPUTER_COST - OLD_CARD_SALE_PRICE + NEW_CARD_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())