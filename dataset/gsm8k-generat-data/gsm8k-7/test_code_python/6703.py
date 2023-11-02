def solution():
    initial_books = 98
    checked_out_on_wednesday = 43
    returned_on_thursday = 23
    checked_out_on_thursday = 5
    returned_on_friday = 7

    # Calculate the total number of books checked out and returned
    total_checked_out = checked_out_on_wednesday + checked_out_on_thursday
    total_returned = returned_on_thursday + returned_on_friday

    # Calculate the total number of books Suzy has on Friday
    total_books = initial_books - total_checked_out + total_returned
    result = total_books
    return result

print(solution())