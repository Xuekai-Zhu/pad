def solution():
    """When Suzy the librarian sat at her desk on Wednesday morning, she had 98 books ready for checkout. The same day, 43 books were checked out. The following day, 23 books were returned, but 5 books were checked out. On Friday, 7 books were returned. How many books did Suzy have?"""
    # Define the initial number of books
    books = 98

    # Subtract the number of books checked out on Wednesday
    books -= 43

    # Add the number of books returned on Thursday
    books += 23

    # Subtract the number of books checked out on Thursday
    books -= 5

    # Add the number of books returned on Friday
    books += 7

    # return the result
    result = books
    return result

print(solution())