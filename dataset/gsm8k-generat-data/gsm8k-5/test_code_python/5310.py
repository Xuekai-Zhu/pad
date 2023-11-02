def solution():
    words_per_minute = 40  # Sarah can read 40 words per minute
    words_per_page = 100  # The books have 100 words per page
    pages_per_book = 80  # The books are 80 pages long
    reading_time = 20 * 60  # Sarah will be reading for 20 hours, converted to minutes

    # Calculate the total number of words Sarah can read
    total_words = words_per_minute * reading_time

    # Calculate the number of books Sarah should check out
    books_to_check_out = total_words // (words_per_page * pages_per_book)

    result = books_to_check_out
    return result

print(solution())