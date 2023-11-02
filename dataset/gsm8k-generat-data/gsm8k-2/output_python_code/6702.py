def solution():
    """When Suzy the librarian sat at her desk on Wednesday morning, she had 98 books ready for checkout. The same day, 43 books were checked out. The following day, 23 books were returned, but 5 books were checked out. On Friday, 7 books were returned. How many books did Suzy have?"""
    starting_books = 98
    checked_out_wed = 43
    returned_thurs = 23
    checked_out_thurs = 5
    returned_fri = 7
    total_books = starting_books - checked_out_wed + returned_thurs - checked_out_thurs + returned_fri
    result = total_books
    return result

print(solution())