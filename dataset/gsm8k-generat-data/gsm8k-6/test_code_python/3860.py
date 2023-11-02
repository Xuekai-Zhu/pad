def solution():
    # Calculate the number of hearts on a standard deck of cards
    hearts_on_deck = 4 * 13  # there are 4 hearts on each of the 13 cards

    # Calculate the number of cows in Devonshire
    cows_in_Devonshire = 2 * hearts_on_deck

    # Calculate the total cost of the cows in Devonshire when sold at $200 each
    total_cost = cows_in_Devonshire * 200
    result = total_cost
    return result

print(solution())