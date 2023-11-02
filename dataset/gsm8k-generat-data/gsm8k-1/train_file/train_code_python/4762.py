def solution():
    """Dave bought 8 books about animals, 6 books about outer space, and 3 books about trains to keep him busy over the holidays. Each book cost $6. How much did Dave spend on the books?"""
    animal_books = 8
    space_books = 6
    train_books = 3
    cost_per_book = 6
    total_books = animal_books + space_books + train_books
    total_cost = total_books * cost_per_book
    result = total_cost
    return result

print(solution())