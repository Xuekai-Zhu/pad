def solution():
    """Dave bought 8 books about animals, 6 books about outer space, and 3 books about trains to keep him busy over the holidays. Each book cost $6. How much did Dave spend on the books?"""
    # Define the cost of each book
    BOOK_COST = 6

    # Define the number of books purchased in each category
    animal_books = 8
    space_books = 6
    train_books = 3

    # Calculate the total cost of all the books
    total_cost = (animal_books + space_books + train_books) * BOOK_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())