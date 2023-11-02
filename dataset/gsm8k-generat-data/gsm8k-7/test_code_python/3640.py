def solution():
    num_cards = 2000
    card_value = 0.05
    comic_book_cost = 6

    # Calculate the total value of all basketball cards
    total_card_value = num_cards * card_value

    # Calculate the maximum number of comic books that can be bought with the total card value
    num_comic_books = int(total_card_value / comic_book_cost)

    # Calculate the total cost of all comic books bought
    comic_book_cost_total = num_comic_books * comic_book_cost

    # Calculate the amount of money Arthur has leftover
    leftover_money = total_card_value - comic_book_cost_total
    result = leftover_money
    return result

print(solution())