def solution():
    total_books = 54  # The book series consists of 54 books
    books_read_first_week = 6  # Cody read 6 books the first week
    books_read_second_week = 3  # Cody read 3 books the second week
    books_read_per_week = 9  # Cody read 9 books per week after the first 2 weeks

    # Calculate the total number of books Cody still needs to read
    books_left_to_read = total_books - (books_read_first_week + books_read_second_week)

    # Calculate the number of weeks it will take Cody to finish reading the series
    weeks_to_finish = books_left_to_read / books_read_per_week

    # Add the first 2 weeks to the total number of weeks
    total_weeks = weeks_to_finish + 2
    result = total_weeks
    return result

print(solution())