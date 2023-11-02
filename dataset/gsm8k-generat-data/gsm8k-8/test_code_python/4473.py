def solution():
    # Calculate the number of unique books Tony and Dean read
    unique_td_books = 23 + 12 - 3 - 1

    # Calculate the number of unique books among all three
    unique_total_books = unique_td_books + 17 - 1  # subtract 1 since they all read the same book

    result = unique_total_books
    return result

print(solution())