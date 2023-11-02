def solution():
    """Ron is part of a book club that allows each member to take a turn picking a new book every week. The club is made up of three couples and five single people along with Ron and his wife. How many times a year does Ron get to pick a new book?"""
    total_people = 3 * 2 + 5 + 2
    total_books_per_year = 52
    ron_books_per_year = (total_books_per_year * 2) / total_people
    result = ron_books_per_year
    return result

print(solution())