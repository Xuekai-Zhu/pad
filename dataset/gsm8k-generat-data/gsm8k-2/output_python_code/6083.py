def solution():
    """There are 15 girls and 10 boys in Ms. Smith's class. She divided 375 books equally among them. How many books did all the girls get combined?"""
    total_students = 15 + 10
    total_books = 375
    books_per_student = total_books / total_students
    total_girls_books = books_per_student * 15
    result = total_girls_books
    return result

print(solution())