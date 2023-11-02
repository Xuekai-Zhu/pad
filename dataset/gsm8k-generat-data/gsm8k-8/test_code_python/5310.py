def solution():
    # Calculate the total number of words Sarah can read in one minute
    words_per_minute = 40

    # Calculate the total number of words in each book
    words_per_book = 100 * 80

    # Calculate the total time Sarah will spend reading in minutes
    total_reading_time = 20 * 60

    # Calculate the total number of words Sarah can read in the time she has
    total_words_read = words_per_minute * total_reading_time

    # Calculate the number of books Sarah should check out
    num_books = total_words_read // words_per_book
    result = num_books
    return result

print(solution())