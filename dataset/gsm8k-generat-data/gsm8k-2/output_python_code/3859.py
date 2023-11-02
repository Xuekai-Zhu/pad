def solution():
    """There are twice as many cows in Devonshire as there are hearts on a standard deck of 52 playing cards. If there are 4 hearts on a card, calculate the total cost of the cows when they are sold at $200 each."""
    hearts_on_deck = 4
    cows_in_devonshire = 2 * hearts_on_deck
    total_cow_cost = cows_in_devonshire * 200
    result = total_cow_cost
    return result

print(solution())