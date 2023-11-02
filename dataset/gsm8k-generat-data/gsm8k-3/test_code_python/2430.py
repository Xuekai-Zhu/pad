def solution():
    """Whitney bought 9 books about whales and 7 books about fish. She also bought 3 magazines. Each book cost $11 and each magazine cost $1. How much did Whitney spend in all?"""
    # Define the cost of each book and magazine
    BOOK_COST = 11
    MAGAZINE_COST = 1

    # Define the number of books and magazines Whitney bought
    whale_books = 9
    fish_books = 7
    magazines = 3

    # Calculate the total cost of the books
    book_cost = (whale_books + fish_books) * BOOK_COST

    # Calculate the total cost of the magazines
    magazine_cost = magazines * MAGAZINE_COST

    # Calculate the total cost of all the items
    total_cost = book_cost + magazine_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())