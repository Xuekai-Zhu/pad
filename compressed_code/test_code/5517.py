def solution():
    
    starting_books = 5
    unhelpful_books = 3
    returned_books = 2
    new_books = 5 + 7
    current_books = starting_books - unhelpful_books + new_books - returned_books
    result = current_books
    return result

print(solution())