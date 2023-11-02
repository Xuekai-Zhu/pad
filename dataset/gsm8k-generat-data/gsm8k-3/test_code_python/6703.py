def solution():
    """When Suzy the librarian sat at her desk on Wednesday morning, she had 98 books ready for checkout. The same day, 43 books were checked out. The following day, 23 books were returned, but 5 books were checked out. On Friday, 7 books were returned. How many books did Suzy have?"""
    # Calculate the number of books checked in and out
    checked_out = 43
    returned1 = 23
    checked_out2 = 5
    returned2 = 7

    # Calculate the net change in the number of books
    net_change = -checked_out + returned1 - checked_out2 + returned2

    # Calculate the final number of books
    final_books = 98 + net_change

    # Display the final number of books
    result = final_books
    return result

print(solution())