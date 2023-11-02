def solution():
    """Josh went to the shopping center. He bought 9 films and 4 books. He also bought 6 CDs. Each film cost $5, each book cost $4 and each CD cost $3. How much did Josh spend in all?"""
    # Define the cost of each item
    FILM_PRICE = 5
    BOOK_PRICE = 4
    CD_PRICE = 3

    # Define the number of each item purchased
    film_count = 9
    book_count = 4
    cd_count = 6

    # Calculate the total cost of the films
    film_cost = film_count * FILM_PRICE

    # Calculate the total cost of the books
    book_cost = book_count * BOOK_PRICE

    # Calculate the total cost of the CDs
    cd_cost = cd_count * CD_PRICE

    # Calculate the total cost of all the items
    total_cost = film_cost + book_cost + cd_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())