def solution():
    """Jack bought 3 books a month at $20 each. He sells them back at the end of the year for $500. How much money did he lose?"""
    books_per_month = 3
    book_price = 20
    total_spent = books_per_month * book_price * 12
    total_earned = 500
    money_lost = total_spent - total_earned
    result = money_lost
    return result

print(solution())