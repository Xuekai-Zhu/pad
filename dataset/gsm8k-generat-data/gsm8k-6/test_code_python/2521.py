def solution():
    # Calculate the number of cards Janet has by setting up an equation based on the information given
    # Let x be the number of cards Brenda has
    # Then Janet has x + 9 cards
    # And Mara has 2(x + 9) cards = 2x + 18 cards
    # Mara has 40 cards less than 150, so 2x + 18 = 150 - 40 = 110
    # Solving for x, we get x = 41
    # Therefore, Brenda has 41 cards, Janet has 50 cards (41 + 9), and Mara has 2*50 = 100 cards
    total_cards = 41 + 50 + 100
    result = total_cards
    return result

print(solution())