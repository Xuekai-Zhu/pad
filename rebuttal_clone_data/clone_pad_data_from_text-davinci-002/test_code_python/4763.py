def solution():
    animal_books = 8
    space_books = 6
    train_books = 3
    book_cost = 6
    total_spent = animal_books * book_cost + space_books * book_cost + train_books * book_cost
    return total_spent

print(solution())