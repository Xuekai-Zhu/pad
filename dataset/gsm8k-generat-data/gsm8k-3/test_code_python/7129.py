def solution():
    """Mary was working on a research paper and already had borrowed 5 books from the library.  3 books weren't helpful so she returned those and checked out 5 more books.  3 days later, she went back to the library and returned 2 of those books and checked out 7 more books.  How many books does Mary currently have checked out of the library?"""
    # Mary had 5 books checked out initially
    num_books = 5

    # Mary returned 3 books and checked out 5 more
    num_books = num_books - 3 + 5

    # Mary returned 2 books and checked out 7 more
    num_books = num_books - 2 + 7

    # Mary currently has this many books checked out
    current_books = num_books

    result = current_books
    return result

print(solution())