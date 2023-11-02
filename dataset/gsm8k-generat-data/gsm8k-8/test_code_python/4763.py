def solution():
    # Define the number of books and the cost per book
    animal_books = 8
    space_books = 6
    train_books = 3
    book_cost = 6
    
    # Calculate the total cost of the books
    total_cost = (animal_books + space_books + train_books) * book_cost
    
    result = total_cost
    return result

print(solution())