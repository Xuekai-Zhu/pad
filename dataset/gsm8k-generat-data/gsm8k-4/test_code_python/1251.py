def solution():
    """Josh went to the shopping center. He bought 9 films and 4 books. He also bought 6 CDs. Each film cost $5, each book cost $4 and each CD cost $3. How much did Josh spend in all?"""
    # Define the prices of films, books, and CDs
    film_price = 5
    book_price = 4
    cd_price = 3

    # Define the number of films, books, and CDs purchased
    num_films = 9
    num_books = 4
    num_cds = 6

    # Calculate the total cost of the purchase
    total_cost = (film_price * num_films) + (book_price * num_books) + (cd_price * num_cds)

    # Return the result
    result = total_cost
    return result

print(solution())