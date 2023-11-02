def solution():
    """Lynne bought 7 books about cats and 2 books about the solar system. She also bought 3 magazines.
    Each book cost 7$ and each magazine cost $4. How much did Lynne spend in all?"""
    # Define the number of books and magazines and their prices
    num_cat_books = 7
    num_solar_books = 2
    num_magazines = 3
    book_price = 7
    magazine_price = 4

    # Calculate the total cost of the books
    total_book_cost = (num_cat_books + num_solar_books) * book_price

    # Calculate the total cost of the magazines
    total_magazine_cost = num_magazines * magazine_price

    # Calculate the total cost of everything
    total_cost = total_book_cost + total_magazine_cost

    # Return the result
    result = total_cost
    return result

print(solution())