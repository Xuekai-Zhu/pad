def solution():
    num_books = 250
    tuesday_out = 120
    wednesday_return = 35
    thursday_out = 15

    # Calculate the total number of books taken out and then returned or withdrawn
    total_change = tuesday_out - wednesday_return - thursday_out

    # Calculate the current number of books in the library
    current_num_books = num_books + total_change
    result = current_num_books
    return result

print(solution())