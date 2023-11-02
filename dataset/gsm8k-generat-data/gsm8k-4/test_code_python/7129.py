def solution():
    """Mary was working on a research paper and already had borrowed 5 books from the library. 3 books weren't helpful so she returned those and checked out 5 more books. 3 days later, she went back to the library and returned 2 of those books and checked out 7 more books. How many books does Mary currently have checked out of the library?"""
    # Define the initial number of books borrowed and returned
    initial_borrowed = 5
    initial_returned = 3

    # Define the number of books borrowed and returned on the second visit
    second_borrowed = 7
    second_returned = 2

    # Calculate the current number of books borrowed
    current_borrowed = initial_borrowed - initial_returned + 5 - second_returned + 7
    # Return the result
    result = current_borrowed
    return result

print(solution())