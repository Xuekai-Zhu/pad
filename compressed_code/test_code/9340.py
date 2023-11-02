def solution():
    
    fantasy_price = 4
    literature_price = fantasy_price / 2
    fantasy_books_sold_per_day = 5
    literature_books_sold_per_day = 8
    total_books_sold_per_day = fantasy_books_sold_per_day + literature_books_sold_per_day
    total_money_per_day = (fantasy_price * fantasy_books_sold_per_day) + (literature_price * literature_books_sold_per_day)
    total_money_after_5_days = total_money_per_day * 5
    result = total_money_after_5_days
    return result

print(solution())