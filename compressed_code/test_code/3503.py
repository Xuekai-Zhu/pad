def solution():
    
    fantasy_price = 4
    literature_price = fantasy_price / 2
    fantasy_books_sold = 5
    literature_books_sold = 8
    total_days = 5
    total_fantasy_earnings = fantasy_price * fantasy_books_sold * total_days
    total_literature_earnings = literature_price * literature_books_sold * total_days
    total_earnings = total_fantasy_earnings + total_literature_earnings
    result = total_earnings
    return result

print(solution())