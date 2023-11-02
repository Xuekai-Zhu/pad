def solution():
    """Arthur wants to sell his basketball card collection and use the money to buy comic books. The store owner tells him that each card is worth 5 cents and comic books cost $6 each. If Arthur sells all 2,000 cards of his and buys as many comic books as he can, how much money does he have leftover?"""
    # Define the price of each card and the price of each comic book
    CARD_PRICE = 0.05
    COMIC_BOOK_PRICE = 6

    # Calculate the total amount of money Arthur gets from selling his basketball card collection
    total_money_from_cards = 2000 * CARD_PRICE

    # Calculate the maximum number of comic books Arthur can buy with the money
    max_num_comic_books = total_money_from_cards // COMIC_BOOK_PRICE

    # Calculate the amount of money Arthur spends on comic books
    total_money_on_comic_books = max_num_comic_books * COMIC_BOOK_PRICE

    # Calculate the amount of money Arthur has left over
    leftover_money = total_money_from_cards - total_money_on_comic_books
    
    result = leftover_money
    return result

print(solution())