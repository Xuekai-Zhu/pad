def solution():
    """Tina is getting $20 for each book she sells. If she realizes a $120 profit on her sales, how many people have she sold the books to if each book costs $5 to make and every customer buys 2 at a time?"""
    # Define the profit per book
    PROFIT_PER_BOOK = 20 - 5 * 2

    # Determine how many books Tina needs to sell to realize a $120 profit
    books_sold = 120 / PROFIT_PER_BOOK

    # Determine how many people Tina has sold the books to
    people_sold_to = books_sold / 2

    # Display the number of people Tina has sold the books to
    result = people_sold_to
    return result

print(solution())