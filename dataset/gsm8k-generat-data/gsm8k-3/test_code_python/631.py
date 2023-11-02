def solution():
    """Mary and Rose went shopping to buy presents. They spent the same amount. Mary bought two pairs of sunglasses for $50 each and a pair of jeans for $100. Rose bought a pair of shoes at $150 and two decks of basketball cards. How much did one deck of basketball cards cost?"""
    # Calculate Mary's total spending
    mary_spending = 2 * 50 + 100

    # Calculate the amount that Rose spent on the two decks of basketball cards
    rose_cards = 150 - (mary_spending / 2)

    # Calculate the cost of one deck of basketball cards
    card_cost = rose_cards / 2

    # Display the cost of one deck of basketball cards
    result = card_cost
    return result

print(solution())