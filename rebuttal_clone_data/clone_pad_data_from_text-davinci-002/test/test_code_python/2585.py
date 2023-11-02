def solution():
    johns_rate = 1.6
    brothers_rate = 1
    hours_to_read_one_book = 8
    number_of_books = 3
    time_for_john = number_of_books * hours_to_read_one_book / johns_rate
    result = time_for_john
    return result

print(solution())