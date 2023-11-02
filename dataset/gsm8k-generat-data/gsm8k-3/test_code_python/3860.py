def solution():
    """There are twice as many cows in Devonshire as there are hearts on a standard deck of 52 playing cards. If there are 4 hearts on a card, calculate the total cost of the cows when they are sold at $200 each."""
    # Calculate the number of hearts on a standard deck of 52 playing cards
    HEARTS_ON_CARD = 4
    num_hearts = HEARTS_ON_CARD * 52

    # Calculate the number of cows in Devonshire
    num_cows = 2 * num_hearts

    # Calculate the total cost of the cows
    cow_cost = num_cows * 200

    # Display the total cost of the cows
    result = cow_cost
    return result

print(solution())