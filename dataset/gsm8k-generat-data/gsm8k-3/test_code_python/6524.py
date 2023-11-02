def solution():
    """Lynne bought 7 books about cats and 2 books about the solar system. She also bought 3 magazines. Each book cost 7$ and each magazine cost $4. How much did Lynne spend in all?"""
    
    # Define the cost of each book and each magazine
    BOOK_COST = 7
    MAGAZINE_COST = 4

    # Define the number of books and magazines bought
    cat_books = 7
    solar_books = 2
    magazines = 3

    # Calculate the total cost of the books
    book_cost = (cat_books + solar_books) * BOOK_COST

    # Calculate the total cost of the magazines
    magazine_cost = magazines * MAGAZINE_COST

    # Calculate the total cost of all the items
    total_cost = book_cost + magazine_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())