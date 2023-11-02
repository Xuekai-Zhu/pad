def solution():
    
    books_per_month = 3
    book_price = 20
    total_spent = books_per_month * book_price * 12
    total_earned = 500
    money_lost = total_spent - total_earned
    result = money_lost
    return result

print(solution())