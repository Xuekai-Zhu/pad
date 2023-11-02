def solution():
    num_films = 9
    num_books = 4
    num_cds = 6
    film_cost = 5
    book_cost = 4
    cd_cost = 3

    # Calculate the total cost of films
    total_film_cost = num_films * film_cost

    # Calculate the total cost of books
    total_book_cost = num_books * book_cost

    # Calculate the total cost of CDs
    total_cd_cost = num_cds * cd_cost

    # Calculate the total cost of all purchases
    total_cost = total_film_cost + total_book_cost + total_cd_cost
    result = total_cost
    return result

print(solution())