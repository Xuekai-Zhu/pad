def solution():
    num_films = 9
    film_price = 5

    num_books = 4
    book_price = 4

    num_cds = 6
    cd_price = 3

    # Calculate the total cost of all films
    total_films_cost = num_films * film_price

    # Calculate the total cost of all books
    total_books_cost = num_books * book_price

    # Calculate the total cost of all CDs
    total_cds_cost = num_cds * cd_price

    # Calculate the total cost of everything Josh bought
    total_cost = total_films_cost + total_books_cost + total_cds_cost
    result = total_cost
    return result

print(solution())