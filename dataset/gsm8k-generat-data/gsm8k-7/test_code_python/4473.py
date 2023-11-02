def solution():
    tony_books = 23
    dean_books = 12
    breanna_books = 17
    shared_books = 3
    all_read_same = 1

    # Calculate the total number of different books read
    total_books = tony_books + dean_books + breanna_books - shared_books - (2 * all_read_same)
    result = total_books
    return result

print(solution())