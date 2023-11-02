def solution():
    """There are twice as many cows in Devonshire as there are hearts on a standard deck of 52 playing cards. If there are 4 hearts on a card, calculate the total cost of the cows when they are sold at $200 each."""
    # Define the number of hearts on a card and the number of cows in Devonshire
    hearts_on_card = 4
    cows_in_devonshire = hearts_on_card * 2 * 52

    # Calculate the total cost of the cows when sold at $200 each
    total_cost = cows_in_devonshire * 200

    # return the result
    result = total_cost
    return result

print(solution())