def solution():
    """Arthur wants to sell his basketball card collection and use the money to buy comic books. The store owner tells him that each card is worth 5 cents and comic books cost $6 each. If Arthur sells all 2,000 cards of his and buys as many comic books as he can, how much money does he have leftover?"""
    card_value = 0.05
    num_cards = 2000
    total_money_from_cards = card_value * num_cards
    comic_book_cost = 6
    num_comic_books = int(total_money_from_cards / comic_book_cost)
    leftover_money = total_money_from_cards - (num_comic_books * comic_book_cost)
    result = leftover_money
    return result

print(solution())