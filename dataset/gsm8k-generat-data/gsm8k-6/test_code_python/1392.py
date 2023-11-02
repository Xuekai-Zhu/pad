def solution():
    # Calculate the number of books Cody has left to read
    books_left = 54 - 6 - 3  # Cody has already read 6 + 3 = 9 books

    # Calculate the number of weeks it will take Cody to finish the series
    weeks_to_finish = books_left / 9

    # Add 2 weeks (the first and second week) to the total number of weeks
    total_weeks = weeks_to_finish + 2
    result = total_weeks
    return result

print(solution())