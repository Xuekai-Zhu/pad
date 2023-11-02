def solution():
    # Define the quantities and prices of the items
    num_films = 9
    film_price = 5
    num_books = 4
    book_price = 4
    num_cds = 6
    cd_price = 3

    # Calculate the total cost of each type of item
    total_film_cost = num_films * film_price
    total_book_cost = num_books * book_price
    total_cd_cost = num_cds * cd_price

    # Calculate the total cost of all items
    total_cost = total_film_cost + total_book_cost + total_cd_cost
    result = total_cost
    return result

print(solution())