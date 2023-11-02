def solution():
    # Calculate the time it takes Peter to read one book
    time_per_book_Peter = 18  # in hours

    # Calculate the time it takes Kristin to read one book
    time_per_book_Kristin = time_per_book_Peter * 3  # Peter reads three times as fast as Kristin

    # Calculate the time it takes Kristin to read half of her books
    books_to_read_Kristin = 20 / 2  # Kristin has to read 10 books
    time_Kristin = time_per_book_Kristin * books_to_read_Kristin

    result = time_Kristin
    return result

print(solution())