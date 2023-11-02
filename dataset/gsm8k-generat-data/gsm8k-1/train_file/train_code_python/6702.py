def solution():
    """When Suzy the librarian sat at her desk on Wednesday morning, she had 98 books ready for checkout. The same day, 43 books were checked out. The following day, 23 books were returned, but 5 books were checked out. On Friday, 7 books were returned. How many books did Suzy have?"""
    initial_books = 98
    checked_out_on_wednesday = 43
    returned_on_thursday = 23
    checked_out_on_thursday = 5
    returned_on_friday = 7
    total_books = initial_books - checked_out_on_wednesday + returned_on_thursday - checked_out_on_thursday + returned_on_friday
    result = total_books
    return result

print(solution())