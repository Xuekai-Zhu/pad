def solution():
    # Calculate the total amount spent by Mary
    mary_total = (2 * 50) + 100  # two pairs of sunglasses for $50 each and a pair of jeans for $100

    # Calculate the amount spent on the pair of shoes by Rose
    rose_shoes = 150

    # Calculate the total amount spent by Rose
    rose_total = mary_total

    # Calculate the amount spent on the two decks of basketball cards by Rose
    cards_total = rose_total - rose_shoes

    # Calculate the cost of one deck of basketball cards
    cost_per_deck = cards_total / 2
    result = cost_per_deck
    return result

print(solution())