def solution():
    cards_with_hearts = 52 / 4  # There are 4 hearts on a standard deck of 52 playing cards
    cows_in_Devonshire = 2 * cards_with_hearts  # There are twice as many cows in Devonshire as there are hearts on a standard deck of 52 playing cards

    # Calculate the total cost of the cows when they are sold at $200 each
    cows_cost = cows_in_Devonshire * 200
    result = cows_cost
    return result

print(solution())