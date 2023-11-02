def solution():
    
    card_value = 0.05
    num_cards = 2000
    money_from_cards = card_value * num_cards
    comic_book_cost = 6
    num_comic_books = int(money_from_cards / comic_book_cost)
    leftover_money = money_from_cards - (num_comic_books * comic_book_cost)
    result = leftover_money
    return result

print(solution())