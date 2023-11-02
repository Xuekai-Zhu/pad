def solution():
    # Define the number of books and students on each day
    total_books = 120
    day1_students = 4
    day2_students = 5
    day3_students = 6

    # Calculate the number of books used on each day
    day1_books = day1_students * 5
    day2_books = day2_students * 5
    day3_books = day3_students * 5

    # Calculate the total number of books used in the first three days
    total_books_used = day1_books + day2_books + day3_books

    # Calculate the number of books remaining in the library
    books_remaining = total_books - total_books_used

    # Calculate the number of students the library can help on the fourth day
    students_on_fourth_day = books_remaining // 5

    result = students_on_fourth_day
    return result

print(solution())