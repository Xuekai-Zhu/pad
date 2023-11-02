def solution():
    # Calculate the total amount of money Arthur gets for selling his card collection
    card_value = 0.05  # value of each card
    total_card_value = card_value * 2000  # value of all cards

    # Calculate the maximum number of comic books Arthur can buy with the money from selling his card collection
    comic_book_price = 6  # price of each comic book
    max_comic_books = total_card_value // comic_book_price  # integer division

    # Calculate the amount of money Arthur has leftover after buying the maximum number of comic books
    leftover_money = total_card_value - (max_comic_books * comic_book_price)

    result = leftover_money
    return result

print(solution())