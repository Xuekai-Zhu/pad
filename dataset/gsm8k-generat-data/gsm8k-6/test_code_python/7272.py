def solution():
    # Calculate the number of books remaining in the library after the first three days
    remaining_books = 120 - (4 * 5 + 5 * 5 + 6 * 5)  # each student needs 5 books
    # Calculate the number of students that can be helped on the fourth day
    students_left = remaining_books // 5
    result = students_left
    return result

print(solution())