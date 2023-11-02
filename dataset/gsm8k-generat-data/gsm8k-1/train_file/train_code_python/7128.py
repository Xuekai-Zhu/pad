def solution():
    """Mary was working on a research paper and already had borrowed 5 books from the library. 3 books weren't helpful so she returned those and checked out 5 more books. 3 days later, she went back to the library and returned 2 of those books and checked out 7 more books. How many books does Mary currently have checked out of the library?"""
    initial_checkouts = 5
    returned_books = 3
    new_checkouts = 5
    returned_again = 2
    final_checkouts = initial_checkouts - returned_books + new_checkouts - returned_again + 7
    result = final_checkouts
    return result

print(solution())