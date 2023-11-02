def solution():
    """Josh went to the shopping center. He bought 9 films and 4 books. He also bought 6 CDs. Each film cost $5, each book cost $4 and each CD cost $3. How much did Josh spend in all?"""
    num_films = 9
    num_books = 4
    num_cds = 6
    film_price = 5
    book_price = 4
    cd_price = 3
    total_price = (num_films * film_price) + (num_books * book_price) + (num_cds * cd_price)
    result = total_price
    return result

print(solution())