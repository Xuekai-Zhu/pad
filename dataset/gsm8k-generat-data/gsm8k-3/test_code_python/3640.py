def solution():
    """Arthur wants to sell his basketball card collection and use the money to buy comic books. The store owner tells him that each card is worth 5 cents and comic books cost $6 each. If Arthur sells all 2,000 cards of his and buys as many comic books as he can, how much money does he have leftover?"""
    # Define the value of each card and the cost of each comic book
    CARD_VALUE = 0.05
    COMIC_BOOK_COST = 6

    # Calculate the total amount of money Arthur can get from selling his cards
    card_total = 2000 * CARD_VALUE

    # Calculate the maximum number of comic books Arthur can buy with the money he gets from selling his cards
    num_comic_books = int(card_total / COMIC_BOOK_COST)

    # Calculate the amount of money Arthur has leftover after buying as many comic books as he can
    leftover_money = card_total - (num_comic_books * COMIC_BOOK_COST)

    # Display the leftover money
    result = leftover_money
    return result

print(solution())