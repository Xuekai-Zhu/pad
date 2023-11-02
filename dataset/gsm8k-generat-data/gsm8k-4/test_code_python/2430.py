def solution():
    """Whitney bought 9 books about whales and 7 books about fish. She also bought 3 magazines. Each book cost $11 and each magazine cost $1. How much did Whitney spend in all?"""
    # Define the cost of each book and magazine
    BOOK_COST = 11
    MAGAZINE_COST = 1

    # Calculate the total cost of the books
    total_book_cost = (9 + 7) * BOOK_COST

    # Calculate the total cost of the magazines
    total_magazine_cost = 3 * MAGAZINE_COST

    # Calculate the total cost of all purchases
    total_cost = total_book_cost + total_magazine_cost

    # return the result
    result = total_cost
    return result

print(solution())