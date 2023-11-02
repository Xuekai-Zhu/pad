def solution():
    # Define the total number of books in the series and the number of books read in the first two weeks
    total_books = 54
    first_week_books = 6
    second_week_books = 3

    # Calculate the remaining number of books that Cody needs to read
    remaining_books = total_books - (first_week_books + second_week_books)

    # Calculate the number of weeks it will take Cody to read the remaining books at a rate of 9 books per week
    weeks_to_finish = remaining_books // 9

    # Add the first two weeks to the total number of weeks needed to finish the series
    total_weeks = weeks_to_finish + 2

    result = total_weeks
    return result

print(solution())