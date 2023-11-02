def solution():
    """Mary was working on a research paper and already had borrowed 5 books from the library. 3 books weren't helpful so she returned those and checked out 5 more books. 3 days later, she went back to the library and returned 2 of those books and checked out 7 more books. How many books does Mary currently have checked out of the library?"""
    starting_books = 5
    unhelpful_books = 3
    returned_books = 2
    new_books = 5 + 7
    current_books = starting_books - unhelpful_books + new_books - returned_books
    result = current_books
    return result

print(solution())