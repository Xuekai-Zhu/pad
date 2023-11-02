def solution():
    total_books = 54
    first_week_books = 6
    second_week_books = 3
    weekly_books = 9

    # Calculate the total number of books read in the first two weeks
    first_two_week_books = first_week_books + second_week_books

    # Calculate the remaining books
    remaining_books = total_books - first_two_week_books

    # Calculate the number of weeks needed to finish the remaining books
    num_weeks = remaining_books / weekly_books

    # Add the first two weeks to the total weeks needed
    total_weeks = 2 + num_weeks
    result = total_weeks
    return result

print(solution())