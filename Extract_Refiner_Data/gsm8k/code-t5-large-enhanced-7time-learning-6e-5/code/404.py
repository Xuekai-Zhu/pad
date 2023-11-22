def solution():
    
    # Define the number of pages and words per page
    PAGES = 45
    WORDS_PER_PAGE = 200

    # Calculate the total number of words read
    total_words = PAGES * WORDS_PER_PAGE

    # Calculate the time it takes to read the book
    book_time = 60 + 10

    # Calculate the time it takes to read the book
    reading_time = total_words / 300

    # Calculate the time early Toby will be
    early_reading_time = reading_time - book_time

    # Display the time early reading
    result = early_reading_time
    return result

print(solution())