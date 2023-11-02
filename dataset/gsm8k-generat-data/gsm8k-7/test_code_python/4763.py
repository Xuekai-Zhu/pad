def solution():
    animal_books = 8
    space_books = 6
    train_books = 3
    book_cost = 6

    # Calculate the total cost of all animal books
    total_animal_cost = animal_books * book_cost

    # Calculate the total cost of all space books
    total_space_cost = space_books * book_cost

    # Calculate the total cost of all train books
    total_train_cost = train_books * book_cost

    # Calculate the total cost of all books
    total_cost = total_animal_cost + total_space_cost + total_train_cost
    result = total_cost
    return result

print(solution())