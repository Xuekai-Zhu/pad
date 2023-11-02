def solution():
    
    lawn_price = 15
    games_price = 45
    books_price = 5
    num_lawns = 35
    total_earned = num_lawns * lawn_price
    games_cost = games_price * 5
    book_money = total_earned - games_cost
    num_books = book_money // books_price
    result = num_books
    return result

print(solution())