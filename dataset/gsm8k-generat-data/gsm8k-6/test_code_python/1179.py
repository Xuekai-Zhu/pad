def solution():
    # Calculate the total number of baseball cards
    total_cards = 40 / (1/3) # Jess has 5 times as many doubles as Rob, so Rob has 1/5 as many doubles as Jess.
    # Therefore, 1/3 of Rob's cards are doubles, so 2/3 of his cards are singles.
    # Let x be the total number of Rob's cards
    # Then, (1/3)x = total_doubles and (2/3)x = total_singles
    # We know that total_doubles = 40, so we can solve for x:
    x = (40 * 3) / 1
    # Therefore, Rob has 120 cards in total.
    result = x
    return result

print(solution())