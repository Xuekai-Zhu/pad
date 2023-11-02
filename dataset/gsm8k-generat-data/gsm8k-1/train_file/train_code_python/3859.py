def solution():
    """There are twice as many cows in Devonshire as there are hearts on a standard deck of 52 playing cards. If there are 4 hearts on a card, calculate the total cost of the cows when they are sold at $200 each."""
    hearts_per_card = 4
    total_hearts = 52 * hearts_per_card
    cows_in_devonshire = 2 * total_hearts
    cow_cost = 200
    total_cow_cost = cows_in_devonshire * cow_cost
    result = total_cow_cost
    return result

print(solution())