def solution():
    # Calculate the total earnings from selling fantasy books and literature books
    fantasy_books_cost = 4
    literature_books_cost = fantasy_books_cost / 2
    fantasy_books_sold = 5
    literature_books_sold = 8
    total_earnings = (fantasy_books_sold * fantasy_books_cost + literature_books_sold * literature_books_cost) * 5

    result = total_earnings
    return result

print(solution())