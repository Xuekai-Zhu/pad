def solution():
    # Calculate the number of hearts on a standard deck of cards
    hearts_on_card = 4
    total_hearts = 52 * hearts_on_card

    # Calculate the number of cows in Devonshire
    cows_in_devonshire = 2 * total_hearts

    # Calculate the total cost of the cows
    cow_cost = 200
    total_cost = cows_in_devonshire * cow_cost
    result = total_cost
    return result

print(solution())